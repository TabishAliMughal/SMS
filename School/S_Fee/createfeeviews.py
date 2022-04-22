from django.shortcuts import redirect, render , get_object_or_404
from School.S_Fee.views import ManageDueFeeView
from School.S_Record.models import Class, ClassSection, FeeTypes
from School.S_Students.models import Student , StudentStatus , StudentFee
from .models import StudentFeeRecord
from .forms import ManageStudentFeeRecordCreateForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateFeeView(request):
    students = Student.objects.all()
    classes = Class.objects.all()
    fee_types = FeeTypes.objects.all()
    form = ManageStudentFeeRecordCreateForm()
    context = {
        'students':students,
        'classes':classes,
        'form':form,
        'fee_types':fee_types,
    }
    return render(request ,'S_Fee/DueFee/Create.html',context)

def check_fee_status(student , month , fee , year):
    try:
        get_object_or_404(StudentFeeRecord , student = student , month = month , fee = fee , year = year)
        return 'added'
    except:
        return 'not_added'

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateStudentFeeView(request):
    student = get_object_or_404(Student , pk = request.POST.get('student'))
    request.POST._mutable = True
    request.POST['status'] = 'Due'
    student_fee = StudentFee.objects.all().filter(student = student.pk)
    message = {'message' : "Student Fee Not Found" , 'type' : 'error' }
    for k in student_fee:
        if int(k.fee_type.pk) == int(request.POST.get('fee_type')):
            request.POST['fee'] = k.pk
            status = check_fee_status(student.pk,request.POST.get('month'),k,request.POST.get('year'))
            if str(status) == 'not_added':
                form = ManageStudentFeeRecordCreateForm(request.POST)
                form.save()
                message = {'message' : "Student Fee Added Successfully" , 'type' : 'success' }
            else:
                message = {'message' : "Student Fee For This Month Already Exist" , 'type' : 'warning' }
    return redirect('student_fee:due_fee_list','Student',message.get('type'),message.get('message'))

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateClassFeeView(request):
    added = []
    not_added = []
    for p in ClassSection.objects.all().filter(clas = request.POST.get('class')):
        for i in Student.objects.all().filter(active = True):
            section = get_object_or_404(StudentStatus , student = i).current_section
            if section == p:
                student = i
                request.POST._mutable = True
                request.POST['status'] = 'Due'
                request.POST['student'] = i
                student_fee = StudentFee.objects.all().filter(student = student.pk , valid = True)
                if student_fee:
                    for k in student_fee:
                        if int(k.fee_type.pk) == int(request.POST.get('fee_type')):
                            request.POST['fee'] = k.pk
                            status = check_fee_status(student.pk,request.POST.get('month'),k,request.POST.get('year'))
                            if str(status) == 'not_added':
                                form = ManageStudentFeeRecordCreateForm(request.POST)
                                form.save()
                                added.append(student)
                            else:
                                not_added.append("{} : Already Exist".format(student))
                        else:
                            if int(request.POST.get('fee_type')) not in [p.fee_type.pk for p in student_fee]:
                                not_added.append("{} : Fee Record Does Not Exist".format(student))
    return ManageDueFeeView(request,'Class',"no","no",added,not_added)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateSelectedClassesFeeView(request):
    added = []
    not_added = []
    for p in Class.objects.all():
        if str(request.POST.get(str(p.pk))) != str(None):
            for p in ClassSection.objects.all().filter(clas = p):
                for i in Student.objects.all().filter(active = True):
                    section = get_object_or_404(StudentStatus , student = i).current_section
                    if section == p:
                        student = i
                        request.POST._mutable = True
                        request.POST['status'] = 'Due'
                        request.POST['student'] = i
                        student_fee = StudentFee.objects.all().filter(student = student.pk , valid = True)
                        if student_fee:
                            for k in student_fee:
                                if int(k.fee_type.pk) == int(request.POST.get('fee_type')):
                                    request.POST['fee'] = k.pk
                                    status = check_fee_status(student.pk,request.POST.get('month'),k,request.POST.get('year'))
                                    if str(status) == 'not_added':
                                        form = ManageStudentFeeRecordCreateForm(request.POST)
                                        form.save()
                                        added.append(student)
                                    else:
                                        not_added.append("{} : Already Exist".format(student))
                                else:
                                    if int(request.POST.get('fee_type')) not in [p.fee_type.pk for p in student_fee]:
                                        not_added.append("{} : Fee Record Does Not Exist".format(student))
    return ManageDueFeeView(request,'Class',"no","no",added,not_added)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateSchoolFeeView(request):
    added = []
    not_added = []
    for i in Student.objects.all().filter(active = True):
        student = i
        request.POST._mutable = True
        request.POST['status'] = 'Due'
        request.POST['student'] = i
        student_fee = StudentFee.objects.all().filter(student = student.pk , valid = True)
        if student_fee:
            for k in student_fee:
                if int(k.fee_type.pk) == int(request.POST.get('fee_type')):
                    request.POST['fee'] = k.pk
                    status = check_fee_status(student.pk,request.POST.get('month'),k,request.POST.get('year'))
                    if str(status) == 'not_added':
                        form = ManageStudentFeeRecordCreateForm(request.POST)
                        form.save()
                        added.append(student)
                    else:
                        not_added.append("{} : Already Exist".format(student))
                else:
                    if int(request.POST.get('fee_type')) not in [p.fee_type.pk for p in student_fee]:
                        not_added.append("{} : Fee Record Does Not Exist".format(student))
    return ManageDueFeeView(request,'School',"no","no",added,not_added)

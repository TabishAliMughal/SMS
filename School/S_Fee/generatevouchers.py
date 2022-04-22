from datetime import datetime
from django.shortcuts import redirect, render , get_object_or_404
import urllib
from School.S_Fee.models import StudentFeeRecord
from School.S_Record.models import Class, FeeTypes
from School.S_School.models import School
from School.S_Students.models import Student, StudentStatus
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageFeeGenerateVouchersView(request,student):
    voucher = []
    url = request.META['HTTP_HOST']
    date = datetime.today()
    for i in student.split('student=')[1:]:
        total_amount_to_pay = int('0')
        i = i.replace("&",'')
        student = get_object_or_404(Student , pk = i)
        fee_records = []
        previous_fee = []
        v = int('0')
        for k in StudentFeeRecord.objects.all().filter(student = student , status = "Due"):
            k.remaining = k.fee.fee - (k.paid_amount or 0)
            fee_records.append(k)
        for k in StudentFeeRecord.objects.all().filter(student = student , status = "PartialyPaid"):
            k.remaining = k.fee.fee - (k.paid_amount or 0)
            fee_records.append(k)
        for k in StudentFeeRecord.objects.all().filter(student = student , status = "Paid").order_by('created'):
            if v != int('8'):
                k.paid = k.paid_amount
                previous_fee.append(k)
                v = v + 1
        student = student
        for v in fee_records:
            total_amount_to_pay = total_amount_to_pay + (v.fee.fee - (v.paid_amount or 0))
        voucher.append({'student':student , 'fee':fee_records , 'total_to_pay':total_amount_to_pay , 'previous_fee':previous_fee})
    context = {
        'date':date,
        'url':url,
        'student':student,
        'voucher':voucher,
        'user':request.user,
        'school':get_object_or_404(School,pk = request.session.get('school').get('pk')),
    }
    return render(request,'S_Fee/Vouchers/Vouchers.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageFeeVouchersView(request):
    students = Student.objects.all()
    classes = Class.objects.all()
    fee_types = FeeTypes.objects.all()
    context = {
        'students':students,
        'classes':classes,
        'fee_types':fee_types,
    }
    return render(request ,'S_Fee/Vouchers/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateStudentFeeVoucherView(request):
    student = get_object_or_404(Student , pk = request.POST.get('student'),active = True)
    record = []
    record.append(student.pk)
    data = (urllib.parse.urlencode({'student':record}, True))
    return redirect('school_fee:generate_fee_vouchers',data)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateClassFeeVoucherView(request):
    record = []
    for i in Student.objects.all().filter(active = True):
        status = get_object_or_404(StudentStatus , student = i , valid = True)
        i.status = status
        if int(status.current_class.pk) == int(request.POST.get('class')):
            record.append(i.pk)
    data = (urllib.parse.urlencode({'student':record}, True))
    return redirect('school_fee:generate_fee_vouchers',data)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateSchoolFeeVoucherView(request):
    record = []
    for i in Student.objects.all().filter(active=True):
        status = get_object_or_404(StudentStatus , student = i , valid = True)
        i.status = status
        record.append(i.pk)
    data = (urllib.parse.urlencode({'student':record}, True))
    return redirect('school_fee:generate_fee_vouchers',data)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageCreateSelectedClassesFeeVoucherView(request):
    record = []
    for i in Student.objects.all().filter(active = True):
        status = get_object_or_404(StudentStatus , student = i , valid = True)
        i.status = status
        for v in Class.objects.all():
            if request.POST.get(str(v.pk)) == 'on':
                if int(status.current_class.pk) == int(v.pk) :
                    record.append(i.pk)
    data = (urllib.parse.urlencode({'student':record}, True))
    return redirect('school_fee:generate_fee_vouchers',data)

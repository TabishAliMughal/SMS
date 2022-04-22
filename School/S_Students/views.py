from django.shortcuts import render , get_object_or_404 , redirect
from App.Authentication.views import GenerateQR
from School.S_Students.models import Student, StudentFee , StudentStatus
from School.S_Record.models import ClassSection , Class , Session , FeeTypes
from School.S_Students.forms import ManageStudentCreateForm , ManageStudentStatusCreateForm , ManageStudentFeeCreateForm
from django.contrib.auth.models import Group , User
from App.Authentication.forms import UserCreationForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageStudentCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(Student , pk = pk)
    else:
        instance = None
    def change_fee(post):
        for i in FeeTypes.objects.all():
            print(request.POST)
            try:
                fee = get_object_or_404(StudentFee , fee_type = i , student = instance , fee = int(request.POST.get('fee{}'.format(i.pk))) , valid = True)
            except:
                try:
                    fee = get_object_or_404(StudentFee , fee_type = i , student = instance , valid = True)
                    fee.valid = False
                    fee.save()
                    StudentFee(student = instance , fee_type = i , fee = int(post.get('fee{}'.format(i.pk)) or '0') , valid = True).save()
                except:
                    StudentFee(student = instance , fee_type = i , fee = int(post.get('fee{}'.format(i.pk)) or '0') , valid = True).save()
    def change_status(post=None):
        try:
            get_object_or_404(StudentStatus , student = instance , valid = True)
        except:
            StudentStatus(student = student ,current_class = get_object_or_404(Class, pk =int(post.get('class_of_admission'))) ,current_section = get_object_or_404(ClassSection , clas = get_object_or_404(Class, pk =int(post.get('class_of_admission'))) , serial = 1) ,current_session = get_object_or_404(Session , pk = post.get('session_of_admission')) ,valid = "True").save()
    if request.method == 'POST':
        student_form = ManageStudentCreateForm(request.POST,request.FILES,instance=instance)
        student = student_form.save()
        change_status(post=request.POST)
        change_fee(post=request.POST)
        return redirect('school_record:gr_register')
    else:
        form = ManageStudentCreateForm(instance=instance)
        if pk:
            form.dob = str(instance.date_of_birth)
            form.doa = str(instance.date_of_admission)
        fee = []
        for i in FeeTypes.objects.all():
            try:
                sel_fee = get_object_or_404(StudentFee , fee_type = i , student = instance , valid = 'True').fee
            except:
                sel_fee = '0'
            fee.append({'type':i,'value':sel_fee})
        form.fee = fee
        users = []
        for i in User.objects.all():
            for p in i.groups.values_list():
                if str(p[1]) == str("School_Student"):
                    try:
                        get_object_or_404(Student , user = i)
                    except:
                        users.append(i)

        form.user_to_add = users
        context = {
            'form' : form ,
        }
        return render(request,'S_Student/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolStudentsListView(request):
    students = []
    for k in Class.objects.all().order_by('serial'):
        clas_students = []
        for j in Student.objects.all().filter(active = "True").order_by('gr_number'):
            try:
                status = get_object_or_404(StudentStatus , student = j , valid = "True" , current_class = k)
                fee = StudentFee.objects.all().filter(student = j , valid = "True")
                j.current_class = status.current_class
                j.current_section = status.current_section
                j.created = status.created
                j.fee = fee
                clas_students.append(j)
            except:
                pass
        students.append({'class': k , 'students': clas_students})
    context = {
        'students':students
    }
    return render(request,'S_Student/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler','School_Teacher'])
def ManageSchoolStudentHistoryView(request,pk):
    student = get_object_or_404(Student ,pk = pk)
    history = StudentStatus.objects.all().filter(student = student).order_by('-created')
    context = {
        'student' : student ,
        'history' : history ,
    }
    return render(request,'S_Student/History.html',context)
    
@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolStudentTransferView(request,pk):
    student = get_object_or_404(Student ,pk = pk)
    try:
        status = get_object_or_404(StudentStatus,student = student,valid=True)
    except:
        status = None
    if request.method == 'POST':
        if status:
            status.valid = False
            status.save()
        form = ManageStudentStatusCreateForm(request.POST)
        form.save()
        return redirect('school_student:student_list')
    else:
        form = ManageStudentStatusCreateForm(instance=status)
        sections = []
        for i in Class.objects.all():
            sections.append({'class':i,'sections':ClassSection.objects.all().filter(clas = i)})
        context = {
            'student' : student ,
            'form' : form ,
            'sections' : sections ,
        }
        return render(request,'S_Student/Transfer.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolStudentManageUserView(request,pk):
    student = get_object_or_404(Student , pk = pk)
    if not student.user:
        if request.method == 'POST':
            try:
                group = Group.objects.get(name='School_Student')
            except:
                group = Group.objects.create(name = "School_Student")
            if request.POST.get('password1') == request.POST.get('password2'):
                form = UserCreationForm(request.POST)
                try:
                    user = form.save()
                    student.user=user
                    student.password = request.POST.get('password1')
                    student.save()
                    user.groups.add(group)
                except:
                    form = UserCreationForm()
                    if student.name.replace(" ","").lower() not in [i.username for i in User.objects.all()]:
                        username = student.name.replace(' ','').lower()
                    else:
                        username = None
                    context = {
                        'student' : student ,
                        'form' : form ,
                        'username' : username ,
                        'message' : "Password Is Not Valid."
                    }
                    return render(request,'S_Student/User/Create.html',context)
            return redirect('school_student:student_list')
        else:
            form = UserCreationForm()
            if student.name.replace(" ","").lower() not in [i.username for i in User.objects.all()]:
                username = student.name.replace(' ','').lower()
            else:
                username = None
            context = {
                'student' : student ,
                'form' : form ,
                'username' : username ,
            }
            return render(request,'S_Student/User/Create.html',context)
    else:
        user = get_object_or_404(User , pk = student.user.pk)
        if request.method == 'POST':
            if request.POST.get('password1') == request.POST.get('password2'):
                from django.contrib.auth.hashers import check_password
                if check_password(request.POST.get('password'),student.user.password) == True :
                    form = UserCreationForm(request.POST or None , instance = user)
                    user = form.save()
                    student.user = user
                    student.password = request.POST.get('password1')
                    student.save()
                    return redirect('school_student:student_list')
                else:
                    form = UserCreationForm(instance = user)
                    message = "Password Is Incorrect"
            else:
                form = UserCreationForm(instance = user)
                message = "Your Passwords Does Not Match"
            context = {
                'student' : student ,
                'form' : form ,
                'message' : message ,
            }
            return render(request,'S_Student/User/ChangePassword.html',context)
        else:
            form = UserCreationForm(instance = user)
            context = {
                'student' : student ,
                'form' : form ,
            }
            return render(request,'S_Student/User/ChangePassword.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolStudentQRGenerateView(request,pk):
    student = get_object_or_404(Student , pk = pk)
    qr = GenerateQR(student.user.username)
    context = {
        'student' : student ,
        'qr' : qr ,
    }
    return render(request,'S_Student/User/QR.html',context)

    
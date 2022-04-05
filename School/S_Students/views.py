from django.shortcuts import render , get_object_or_404 , redirect
from School.S_Students.models import Student , StudentStatus
from School.S_Record.models import ClassSection , Class , Session
from School.S_Students.forms import ManageStudentCreateForm , ManageStudentStatusCreateForm
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
    if request.method == 'POST':
        student_form = ManageStudentCreateForm(request.POST,request.FILES,instance=instance)
        student = student_form.save()
        if not instance:
            status_form = ManageStudentStatusCreateForm({
                'student' : student ,
                'current_class' : request.POST.get('class_of_admission') ,
                'current_section' : int("1") ,
                'current_session' : request.POST.get('session_of_admission') ,
                'valid' : "True" ,
            })
            status_form.save()
        return redirect('school_record:gr_register')
    else:
        form = ManageStudentCreateForm(instance=instance)
        if pk:
            form.dob = str(instance.date_of_birth)
            form.doa = str(instance.date_of_admission)
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
                j.current_class = status.current_class
                j.current_section = status.current_section
                j.created = status.created
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

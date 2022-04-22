from django.shortcuts import render , get_object_or_404 , redirect
from School.S_Teachers.models import Teacher , TeacherSubject , TeacherClass , TeacherSalary
from .forms import ManageTeacherCreateForm , ManageTeacherSalaryCreateForm , ManageTeacherClassCreateForm , ManageTeacherSubjectCreateForm
import datetime
from django.contrib.auth.models import Group , User
from App.Authentication.forms import UserCreationForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeachersListView(request):
    teachers = []
    for i in Teacher.objects.all().order_by('pk'):
        i.clas = get_object_or_404(TeacherClass , teacher = i , valid = 'True')
        i.salary = get_object_or_404(TeacherSalary , teacher = i , valid = 'True')
        i.subjects = get_object_or_404(TeacherSubject , teacher = i , valid = 'True')
        teachers.append(i)
    context = {
        'teachers':teachers
    }
    return render(request,'S_Teacher/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(Teacher , pk = pk)
        salary_instance = get_object_or_404(TeacherSalary , teacher = instance , valid = True)
        class_instance = get_object_or_404(TeacherClass , teacher = instance , valid = True)
        subject_instance = get_object_or_404(TeacherSubject , teacher = instance , valid = True)
    else:
        instance = None
        salary_instance = None
        class_instance = None
        subject_instance = None
    if request.method == 'POST':
        teacher_form = ManageTeacherCreateForm(request.POST,request.FILES,instance=instance)
        teacher = teacher_form.save()
        request.POST._mutable = True
        request.POST['teacher'] = teacher
        request.POST['valid'] = True
        TeacherSalary.objects.all().filter(teacher = teacher).update(valid = "False")
        salary_form = ManageTeacherSalaryCreateForm(request.POST)
        salary_form.save()
        TeacherClass.objects.all().filter(teacher = teacher).update(valid = "False")
        class_form = ManageTeacherClassCreateForm(request.POST)
        class_form.save()
        TeacherSubject.objects.all().filter(teacher = teacher).update(valid = "False")
        subject_form = ManageTeacherSubjectCreateForm(request.POST)
        subject_form.save()
        return redirect('school_teacher:teacher_list')
    else:
        form = ManageTeacherCreateForm(instance=instance)
        salary_form = ManageTeacherSalaryCreateForm(instance = salary_instance)
        class_form = ManageTeacherClassCreateForm(instance = class_instance)
        subject_form = ManageTeacherSubjectCreateForm(instance = subject_instance)
        if pk:
            form.doi = str(instance.date_of_interview)
            form.doj = str(instance.date_of_joining)
            form.dob = str(instance.date_of_birth)
        context = {
            'form' : form ,
            'salary_form' : salary_form ,
            'class_form' : class_form ,
            'subject_form' : subject_form ,
        }
        return render(request,'S_Teacher/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherClassCreateView(request,pk):
    teacher = get_object_or_404(Teacher , pk = pk)
    instance = get_object_or_404(TeacherClass , teacher = pk , valid = True)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = teacher
        request.POST['valid'] = 'True'
        TeacherClass.objects.all().filter(teacher = teacher).update(valid="False")
        form = ManageTeacherClassCreateForm(request.POST)
        form.save()
        return redirect('school_teacher:teacher_list')
    else:
        form = ManageTeacherClassCreateForm(instance = instance)
        context = {
            'form' : form ,
        }
        return render(request,'S_Teacher/Status/TeacherClass.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherSubjectCreateView(request,pk):
    teacher = get_object_or_404(Teacher , pk = pk)
    instance = get_object_or_404(TeacherSubject , teacher = pk , valid = True)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = teacher
        request.POST['valid'] = 'True'
        TeacherSubject.objects.all().filter(teacher = teacher).update(valid="False")
        form = ManageTeacherSubjectCreateForm(request.POST)
        form.save()
        return redirect('school_teacher:teacher_list')
    else:
        form = ManageTeacherSubjectCreateForm(instance = instance)
        context = {
            'form' : form ,
        }
        return render(request,'S_Teacher/Status/TeacherSubject.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherSalaryCreateView(request,pk):
    teacher = get_object_or_404(Teacher , pk = pk)
    instance = get_object_or_404(TeacherSalary , teacher = pk , valid = True)
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = teacher
        request.POST['valid'] = 'True'
        TeacherSalary.objects.all().filter(teacher = teacher).update(valid="False")
        form = ManageTeacherSalaryCreateForm(request.POST)
        form.save()
        return redirect('school_teacher:teacher_list')
    else:
        form = ManageTeacherSalaryCreateForm(instance = instance)
        context = {
            'form' : form ,
        }
        return render(request,'S_Teacher/Status/TeacherSalary.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageTeacherHistoryView(request,pk):
    teacher = get_object_or_404(Teacher , pk = pk)
    history = []
    for i in TeacherSalary.objects.all().filter(teacher = teacher):
        history.append({
            'salary' : i.salary ,
            'valid' : i.valid ,
            'created' : str(i.created)[:19] ,
        })
    for i in TeacherClass.objects.all().filter(teacher = teacher):
        history.append({
            'clas' : i.clas ,
            'valid' : i.valid ,
            'created' : str(i.created)[:19] ,
        })
    for i in TeacherSubject.objects.all().filter(teacher = teacher):
        history.append({
            'subjects' : i.subjects ,
            'valid' : i.valid ,
            'created' : str(i.created)[:19] ,
        })
    history = sorted(history, key=lambda t: datetime.datetime.strptime(t.get('created'), '%Y-%m-%d %H:%M:%S'))[::-1]
    context = {
        'teacher' : teacher ,
        'history' : history ,
    }
    return render(request,'S_Teacher/History.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolTeacherManageUserView(request,pk):
    teacher = get_object_or_404(Teacher , pk = pk)
    if not teacher.user:
        if request.method == 'POST':
            try:
                group = Group.objects.get(name='School_Teacher')
            except:
                group = Group.objects.create(name = "School_Teacher")
            if request.POST.get('password1') == request.POST.get('password2'):
                form = UserCreationForm(request.POST)
                try:
                    user = form.save()
                    teacher.user=user
                    teacher.password = request.POST.get('password1')
                    teacher.save()
                    user.groups.add(group)
                except:
                    form = UserCreationForm()
                    if teacher.name.replace(" ","").lower() not in [i.username for i in User.objects.all()]:
                        username = teacher.name.replace(' ','').lower()
                    else:
                        username = None
                    context = {
                        'student' : teacher ,
                        'form' : form ,
                        'username' : username ,
                        'message' : "Password Is Not Valid."
                    }
                    return render(request,'S_Teacher/User/Create.html',context)
            return redirect('school_teacher:teacher_list')
        else:
            form = UserCreationForm()
            if teacher.name.replace(" ","").lower() not in [i.username for i in User.objects.all()]:
                username = teacher.name.replace(' ','').lower()
            else:
                username = None
            context = {
                'student' : teacher ,
                'form' : form ,
                'username' : username ,
            }
            return render(request,'S_Teacher/User/Create.html',context)
    else:
        user = get_object_or_404(User , pk = teacher.user.pk)
        if request.method == 'POST':
            if request.POST.get('password1') == request.POST.get('password2'):
                from django.contrib.auth.hashers import check_password
                if check_password(request.POST.get('password'),teacher.user.password) == True :
                    form = UserCreationForm(request.POST or None , instance = user)
                    user = form.save()
                    teacher.user = user
                    teacher.password = request.POST.get('password1')
                    teacher.save()
                    return redirect('school_teacher:teacher_list')
                else:
                    form = UserCreationForm(instance = user)
                    message = "Password Is Incorrect"
            else:
                form = UserCreationForm(instance = user)
                message = "Your Passwords Does Not Match"
            context = {
                'student' : teacher ,
                'form' : form ,
                'message' : message ,
            }
            return render(request,'S_Teacher/User/ChangePassword.html',context)

        else:
            form = UserCreationForm(instance = user)
            context = {
                'student' : teacher ,
                'form' : form ,
            }
            return render(request,'S_Teacher/User/ChangePassword.html',context)

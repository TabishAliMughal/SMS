import datetime
from django.shortcuts import get_object_or_404, redirect, render
from School.S_Record.models import ClassSection
from Student.I_Students.views import get_student
from School.S_Homework.models import Homework , HomeworkImage , HomeworkVideo
from .models import StudentHomeworkStatus
from .forms import ManageStudentHomeworkStatusCreateForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Student'])
def ManageStudentHomeworkList(request):
    student = get_student(request)
    homework = []
    for i in Homework.objects.all().filter(clas = get_object_or_404(ClassSection , pk = student.current_section.pk)).order_by('created'):
        i.images = HomeworkImage.objects.all().filter(homework = i)
        i.video = HomeworkVideo.objects.all().filter(homework = i)
        try:
            i.status = get_object_or_404(StudentHomeworkStatus , student = student , homework = i)
        except:
            i.status = None
        homework.append(i)
    today_homework = []
    previous_homework = []
    for i in homework:
        if i.date == datetime.date.today():
            today_homework.append(i)
        else:
            previous_homework.append(i)
    context = {
        'student':student,
        'homework':homework,
        'today_homework':today_homework,
        'previous_homework':previous_homework,
    }
    return render(request ,'I_Homework/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Student'])
def ManageStudentHomeworkDetail(request,pk):
    homework = get_object_or_404(Homework , pk = pk)
    homework.images = HomeworkImage.objects.all().filter(homework = homework)
    homework.video = HomeworkVideo.objects.all().filter(homework = homework)
    context = {
        'homework':homework,
    }
    return render(request ,'I_Homework/Detail.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Student'])
def ManageStudentHomeworkStart(request,pk):
    homework = get_object_or_404(Homework , pk = pk)
    homework_status_form = ManageStudentHomeworkStatusCreateForm({
        'student': get_student(request) ,
        'homework': homework ,
        'status': False ,
    })
    homework_status_form.save()
    return redirect('student_homework:homework_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Student'])
def ManageStudentHomeworkComplete(request,pk):
    homework = get_object_or_404(Homework , pk = pk)
    status = get_object_or_404(StudentHomeworkStatus , student = get_student(request) , homework = homework)
    status.status = True
    status.save()
    return redirect('student_homework:homework_list')


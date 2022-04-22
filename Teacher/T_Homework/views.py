from django.shortcuts import get_object_or_404, render , redirect
from School.S_Homework.models import Homework, HomeworkImage, HomeworkVideo
from Student.I_Homework.models import StudentHomeworkStatus
from Teacher.T_Teachers.views import  get_teacher
from Teacher.T_Students.views import get_students
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required
from School.S_Homework.forms import ManageHomeworkCreateForm , ManageHomeworkImageCreateForm , ManageHomeworkVideoCreateForm


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherClassHomeworklList(request):
    teacher = get_teacher(request)
    homework = []
    for i in Homework.objects.all().filter(teacher = teacher).order_by('clas'):
        i.images = HomeworkImage.objects.all().filter(homework = i)
        i.video = HomeworkVideo.objects.all().filter(homework = i)
        homework.append(i)
        completed_students = []
        incompleted_students = []
        for j in get_students(teacher):
            try:
                i.status = get_object_or_404(StudentHomeworkStatus , student = j , homework = i)
                completed_students.append(j)
            except:
                i.status = None
                incompleted_students.append(j)
        i.status = {'completed':completed_students , 'incomplete':incompleted_students , 'completed_count':len(completed_students) , 'incomplete_count':len(incompleted_students)}
    context = {
        'teacher':teacher,
        'homework':homework,
    }
    return render(request ,'T_Homework/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherClassHomeworklDetail(request,pk):
    homework = get_object_or_404(Homework , pk = pk)
    homework.images = HomeworkImage.objects.all().filter(homework = homework)
    homework.video = HomeworkVideo.objects.all().filter(homework = homework)
    context = {
        'homework':homework,
    }
    return render(request ,'T_Homework/Detail.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherClassHomeworklCreate(request):
    teacher = get_teacher(request)
    if request.method == 'POST':
        print(request.POST)
        request.POST._mutable = True
        request.POST['teacher'] = teacher
        homework_form = ManageHomeworkCreateForm(request.POST)
        homework = homework_form.save()
        request.POST['homework'] = homework
        for i in range(0,len(request.FILES.getlist('image'))):
            if request.FILES.getlist('image')[i]:
                homework_image_form = ManageHomeworkImageCreateForm({
                    'homework':homework,
                    'text':request.POST.getlist('img_text')[i],
                },{
                    'image':request.FILES.getlist('image')[i],
                })
                homework_image_form.save()
        for i in range(0,len(request.POST.getlist('video'))):
            if request.POST.getlist('video')[i]:
                homework_video_form = ManageHomeworkVideoCreateForm({
                    'homework':homework,
                    'video':request.POST.getlist('video')[i],
                    'text':request.POST.getlist('vid_text')[i],
                })
                homework_video_form.save()
        return redirect('teacher_homework:homework_list')
    else:
        homework_form = ManageHomeworkCreateForm()
        homework_image_form = ManageHomeworkImageCreateForm()
        homework_video_form = ManageHomeworkVideoCreateForm()

        context = {
            'homework_form' : homework_form ,
            'homework_image_form' : homework_image_form ,
            'homework_video_form' : homework_video_form ,
        }
        return render(request , 'T_Homework/Create.html',context)

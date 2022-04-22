from django.shortcuts import render , redirect , get_object_or_404
from School.S_Teachers.models import Teacher , TeacherClass , TeacherSalary , TeacherSubject , TeacherDetail , TeacherAlbumImages , TeacherAlbumVideos
from School.S_Teachers.forms import ManageTeacherDetailCreateForm , ManageTeacherAlbumImagesCreateForm , ManageTeacherAlbumVideosCreateForm
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

def get_teacher(request):
    teacher = get_object_or_404(Teacher , user = request.user)
    teacher.clas = get_object_or_404(TeacherClass , teacher = teacher , valid = 'True')
    teacher.salary = get_object_or_404(TeacherSalary , teacher = teacher , valid = 'True')
    teacher.subjects = get_object_or_404(TeacherSubject , teacher = teacher , valid = 'True')
    return teacher

def ManageTeacherProfileView(request):
    teacher = get_teacher(request)
    detail = TeacherDetail.objects.all().filter(valid = True)
    images = []
    v = int('0')
    for i in TeacherAlbumImages.objects.all().filter(valid = True):
        v = v + 1
        images.append({'image':i , 'count': v})
    videos = []
    v = int('0')
    for i in TeacherAlbumVideos.objects.all().filter(valid = True):
        v = v + 1
        videos.append({'video':i , 'count': v})
    context = {
        'teacher' : teacher ,
        'detail' : detail ,
        'images' : images ,
        'videos' : videos ,
    }
    return render(request , 'T_Teacher/Profile.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherDetailListView(request):
    detail = TeacherDetail.objects.all().order_by('valid').filter(teacher = get_teacher(request))
    context = {
        'detail' : detail ,
    }
    return render(request,'T_Profile/Detail/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherDetailCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(TeacherDetail , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = get_teacher(request)
        form = ManageTeacherDetailCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('teacher:detail_list')
    else:
        form = ManageTeacherDetailCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'T_Profile/Detail/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherDetailChangeStatusView(request,pk):
    instance = get_object_or_404(TeacherDetail , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('teacher:detail_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumImagesListView(request):
    images = TeacherAlbumImages.objects.all().order_by('valid').filter(teacher = get_teacher(request))
    context = {
        'images' : images ,
    }
    return render(request,'T_Profile/Album/Images/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumImagesCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(TeacherAlbumImages , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = get_teacher(request)
        form = ManageTeacherAlbumImagesCreateForm(request.POST,request.FILES,instance = instance)
        print(form)
        form.save()
        return redirect('teacher:album_images_list')
    else:
        form = ManageTeacherAlbumImagesCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'T_Profile/Album/Images/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumImagesChangeStatusView(request,pk):
    instance = get_object_or_404(TeacherAlbumImages , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('teacher:album_images_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumVideosListView(request):
    videos = TeacherAlbumVideos.objects.all().order_by('valid').filter(teacher = get_teacher(request))
    context = {
        'videos' : videos ,
    }
    return render(request,'T_Profile/Album/Videos/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumVideosCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(TeacherAlbumVideos , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['teacher'] = get_teacher(request)
        form = ManageTeacherAlbumVideosCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('teacher:album_videos_list')
    else:
        form = ManageTeacherAlbumVideosCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'T_Profile/Album/Videos/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherAlbumVideosChangeStatusView(request,pk):
    instance = get_object_or_404(TeacherAlbumVideos , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('teacher:album_videos_list')

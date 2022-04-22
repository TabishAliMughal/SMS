from django.shortcuts import get_object_or_404, redirect, render
from School.S_School.models import School
from School.S_Record.models import ClassSection, Class, ClassSubjects , Session, Subject , SchoolDetail , SchoolAlbumImages , SchoolAlbumVideos , SchoolAnnouncements , SchoolFeeStructure
from School.S_Record.forms import ManageClassSectionCreateForm, ManageClassCreateForm, ManageClassSubjectCreateForm , ManageSessionCreateForm, ManageSubjectCreateForm , ManageSchoolDetailCreateForm , ManageSchoolAlbumImagesCreateForm , ManageSchoolAlbumVideosCreateForm , ManageSchoolAnnouncementsCreateForm , ManageSchoolFeeStructureCreateForm
from School.S_Students.models import Student , StudentStatus
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolGrRegisterView(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request,'S_Record/GrRegister.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassListView(request):
    classes = []
    for i in Class.objects.all().order_by('serial'):
        i.sections = len(ClassSection.objects.all().filter(clas=i))
        classes.append(i)
    context = {
        'class':classes,
    }
    return render(request,"S_Record/Class/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(Class , pk = pk)
    else:
        instance = None
    if request.method == "POST":
        form = ManageClassCreateForm(request.POST,instance=instance)
        clas = form.save()
        form = ManageClassSectionCreateForm({
            'serial' : 1 ,
            'name' : "Section 1" ,
            'clas' : clas ,
        })
        form.save()
        return redirect('school_record:class_list')
    else:
        form = ManageClassCreateForm(instance=instance)
        context = {
            'form' : form ,
        }
        return render(request,"S_Record/Class/Create.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSessionListView(request):
    session = Session.objects.all().order_by('serial')
    context = {
        'session':session,
    }
    return render(request,"S_Record/Session/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSessionCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(Session , pk = request.POST.get('pk'))
    else:
        instance = None
    if request.method == "POST":
        form = ManageSessionCreateForm(request.POST,instance=instance)
        form.save()
        return redirect('school_record:session_list')
    else:
        form = ManageSessionCreateForm(instance=instance)
        context = {
            'form' : form ,
        }
        return render(request,"S_Record/Session/Create.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassSectionListView(request,pk):
    clas = get_object_or_404(Class , pk = pk)
    class_section = ClassSection.objects.all().filter(clas = clas).order_by('serial')
    context = {
        'class_section':class_section,
        'class':clas,
    }
    return render(request,"S_Record/ClassSection/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassSectionCreateView(request,clas=None,pk=None):
    if pk:
        instance = get_object_or_404(ClassSection , pk = pk)
        form = ManageClassSectionCreateForm(instance=instance)
    else:
        instance = None
        form = ManageClassSectionCreateForm(instance=ClassSection(clas = get_object_or_404(Class , pk = clas)))
    if request.method == "POST":
        if clas:
            request.POST._mutable = True
            request.POST['clas'] = get_object_or_404(Class , pk = clas).pk
        form = ManageClassSectionCreateForm(request.POST or None,instance=instance)
        form.save()
        return redirect('school_record:class_list')
    else:
        context = {
            'form' : form ,
        }
        return render(request,"S_Record/ClassSection/Create.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSubjectListView(request):
    subject = Subject.objects.all()
    context = {
        'subject':subject,
    }
    return render(request,"S_Record/Subject/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSubjectCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(Subject , pk = pk)
    else:
        instance = None
    if request.method == "POST":
        form = ManageSubjectCreateForm(request.POST or None,instance=instance)
        form.save()
        return redirect('school_record:subject_list')
    else:
        form = ManageSubjectCreateForm(instance=instance)
        context = {
            'form' : form ,
        }
        return render(request,"S_Record/Subject/Create.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassSubjectListView(request):
    class_subject = ClassSubjects.objects.all()
    context = {
        'class_subject':class_subject,
    }
    return render(request,"S_Record/ClassSubjects/List.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageClassSubjectCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(ClassSubjects , pk = pk)
    else:
        instance = None
    if request.method == "POST":
        form = ManageClassSubjectCreateForm(request.POST or None,instance=instance)
        form.save()
        return redirect('school_record:class_subject_list')
    else:
        form = ManageClassSubjectCreateForm(instance=instance)
        context = {
            'form' : form ,
        }
        return render(request,"S_Record/ClassSubjects/Create.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolDetailListView(request):
    detail = SchoolDetail.objects.all().order_by('valid')
    context = {
        'detail' : detail ,
    }
    return render(request,'S_Profile/Detail/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolDetailCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(SchoolDetail , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        form = ManageSchoolDetailCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('school_record:detail_list')
    else:
        form = ManageSchoolDetailCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'S_Profile/Detail/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolDetailChangeStatusView(request,pk):
    instance = get_object_or_404(SchoolDetail , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('school_record:detail_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumImagesListView(request):
    images = SchoolAlbumImages.objects.all().order_by('valid')
    context = {
        'images' : images ,
    }
    return render(request,'S_Profile/Album/Images/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumImagesCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(SchoolAlbumImages , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        form = ManageSchoolAlbumImagesCreateForm(request.POST,request.FILES,instance = instance)
        form.save()
        return redirect('school_record:album_images_list')
    else:
        form = ManageSchoolAlbumImagesCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'S_Profile/Album/Images/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumImagesChangeStatusView(request,pk):
    instance = get_object_or_404(SchoolAlbumImages , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('school_record:album_images_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumVideosListView(request):
    videos = SchoolAlbumVideos.objects.all().order_by('valid')
    context = {
        'videos' : videos ,
    }
    return render(request,'S_Profile/Album/Videos/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumVideosCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(SchoolAlbumVideos , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        form = ManageSchoolAlbumVideosCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('school_record:album_videos_list')
    else:
        form = ManageSchoolAlbumVideosCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'S_Profile/Album/Videos/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAlbumVideosChangeStatusView(request,pk):
    instance = get_object_or_404(SchoolAlbumVideos , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('school_record:album_videos_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAnnouncementsListView(request):
    announcements = SchoolAnnouncements.objects.all().order_by('valid')
    context = {
        'announcements' : announcements ,
    }
    return render(request,'S_Profile/Announcements/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAnnouncementsCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(SchoolAnnouncements , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        form = ManageSchoolAnnouncementsCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('school_record:announcements_list')
    else:
        form = ManageSchoolAnnouncementsCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'S_Profile/Announcements/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolAnnouncementsChangeStatusView(request,pk):
    instance = get_object_or_404(SchoolAnnouncements , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('school_record:announcements_list')

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolFeeStructureListView(request):
    fee = SchoolFeeStructure.objects.all().order_by('valid')
    context = {
        'fee' : fee ,
    }
    return render(request,'S_Profile/FeeStructure/List.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolFeeStructureCreateView(request,pk=None):
    if pk:
        instance = get_object_or_404(SchoolFeeStructure , pk = pk)
    else:
        instance = None
    if request.method == 'POST':
        form = ManageSchoolFeeStructureCreateForm(request.POST,instance = instance)
        form.save()
        return redirect('school_record:fee_structure_list')
    else:
        form = ManageSchoolFeeStructureCreateForm(instance = instance)
        context = {
            'form':form,
        }
        return render(request,'S_Profile/FeeStructure/Create.html',context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Owner','School_Data_Handeler'])
def ManageSchoolFeeStructureChangeStatusView(request,pk):
    instance = get_object_or_404(SchoolFeeStructure , pk = pk)
    if str(instance.valid) == "False":
        instance.valid = True
    else:
        instance.valid = False
    instance.save()
    return redirect('school_record:fee_structure_list')

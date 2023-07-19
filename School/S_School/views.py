from django.shortcuts import get_object_or_404, redirect, render
from School.S_School.models import School
from .forms import ManageSchoolCreateForm , ManageDomainCreateForm
from App.Authentication.forms import CreateUserForm
from tenant_schemas.utils import tenant_context
from django.contrib.auth.models import Group
from App.Authentication.user_handeling import allowed_users
from django.db import connection
from django.contrib.auth.decorators import login_required
from School.S_Record.models import SchoolDetail , SchoolAlbumImages , SchoolAlbumVideos , SchoolAnnouncements , SchoolFeeStructure

def AddUserToGroup(user,group):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO auth_user_groups (user_id , group_id) VALUES ( {} , {} )".format(user , group))
    return

def ManageSchoolProfileView(request,rejected=None):
    site = request.META['HTTP_HOST']
    school = get_object_or_404(School , schema_name = site.split(".")[0])
    request.session['school'] = {
        'pk' : school.pk ,
        'short_name' : school.short_name ,
        'full_name' : school.full_name ,
        'principal_name' : school.principal_name ,
        'active' : school.active ,
    }
    request.session.save()
    detail = SchoolDetail.objects.all().filter(valid = True)
    images = []
    v = int('0')
    for i in SchoolAlbumImages.objects.all().filter(valid = True):
        v = v + 1
        images.append({'image':i , 'count': v})
    videos = []
    v = int('0')
    for i in SchoolAlbumVideos.objects.all().filter(valid = True):
        v = v + 1
        videos.append({'video':i , 'count': v})
    announcements = SchoolAnnouncements.objects.all().filter(valid = True)
    fee = SchoolFeeStructure.objects.all().filter(valid = True)
    context = {
        'detail' : detail ,
        'images' : images ,
        'videos' : videos ,
        'announcements' : announcements ,
        'fee' : fee ,
    }
    if rejected:
        context['message'] = "User Not Found"
    return render(request , "S_School/Profile.html",context)

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['Admin'])
def ManageSchoolCreateView(request):
    domain_form = ManageDomainCreateForm()
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['schema_name'] = request.POST.get('short_name').lower()
        school_form = ManageSchoolCreateForm(request.POST,request.FILES)
        if str(request.POST.get('short_name').lower()) not in [i.schema_name for i in School.objects.all()]:
            tenant = school_form.save()
            domain_form = ManageDomainCreateForm({
                'domain' : str("{}.{}".format(request.POST.get('schema_name'),request.META['HTTP_HOST'])) ,
                'tenant' : tenant ,
                'is_primary' : True ,
            })
            domain_form.save()
            with tenant_context(tenant):
                user_form = CreateUserForm({
                    'username' : "Admin1" ,
                    'email' : "" ,
                    'password1' : "abc123xyz" ,
                    'password2' : "abc123xyz" ,
                })
                school_user = user_form.save()
                school_user.is_staff = "True"
                school_user.is_superuser = "False"
                school_user.save()
                try:
                    Group.objects.get(name='School_Owner')
                except:
                    Group.objects.create(name = "School_Owner")
                group = Group.objects.get(name='School_Owner')
                AddUserToGroup(school_user.pk,group.id)
                user_form = CreateUserForm({
                    'username' : "ComsoftSystems" ,
                    'email' : "" ,
                    'password1' : "CSS@abc123xyz" ,
                    'password2' : "CSS@abc123xyz" ,
                })
                super_user = user_form.save()
                super_user.is_staff = "True"
                super_user.is_superuser = "True"
                super_user.save()
                try:
                    Group.objects.get(name='School_Owner')
                except:
                    Group.objects.create(name = "School_Owner")
                group = Group.objects.get(name='School_Owner')
                AddUserToGroup(super_user.pk,group.id)
        else:
            context = {
                'form' : school_form,
                'message' : "School Short Name Already Exist",
            }
            return render(request , "S_School/Create.html",context)
        return redirect('main:main')
    else:
        school_form = ManageSchoolCreateForm()
        context = {
            'form' : school_form ,
        }
        return render(request , "S_School/Create.html",context)

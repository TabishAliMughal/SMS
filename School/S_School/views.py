from django.shortcuts import get_object_or_404, redirect, render
from School.S_School.models import School
from .forms import ManageSchoolCreateForm , ManageDomainCreateForm
from App.Authentication.forms import UserCreationForm
from tenant_schemas.utils import tenant_context
from django.contrib.auth.models import Group
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


def ManageSchoolProfileView(request):
    site = request.META['HTTP_HOST'].split(":")[0]
    school = get_object_or_404(School , schema_name = site.split(".")[0])
    request.session['school'] = {
        'pk' : school.pk ,
        'short_name' : school.short_name ,
        'full_name' : school.full_name ,
        'principal_name' : school.principal_name ,
        'active' : school.active ,
    }
    request.session.save()
    context = {
    }
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
                'domain' : str("{}.{}".format(request.POST.get('schema_name'),request.META['HTTP_HOST'].split(":")[0])) ,
                'tenant' : tenant ,
                'is_primary' : True ,
            })
            domain_form.save()
            with tenant_context(tenant):
                user_form = UserCreationForm({
                    'username' : "Admin1" ,
                    'email' : "" ,
                    'password1' : "abc123xyz" ,
                    'password2' : "abc123xyz" ,
                })
                user = user_form.save()
                user.is_staff = "True"
                user.is_superuser = "True"
                user.save()
                try:
                    Group.objects.get(name='School_Owner')
                except:
                    Group.objects.create(name = "School_Owner")
                group = Group.objects.get(name='School_Owner')
                user.groups.add(group)
        else:
            context = {
                'form' : school_form,
                'message' : "School Short Name Already Exist",
            }
            return render(request , "School/Create.html",context)
        return redirect('main:main')
    else:
        school_form = ManageSchoolCreateForm()
        context = {
            'form' : school_form ,
        }
        return render(request , "S_School/Create.html",context)

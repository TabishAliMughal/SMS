from django.shortcuts import get_object_or_404, render , redirect

from School.S_School.models import School , Domain


def ManageMainPageView(request):
    if request.user.is_authenticated and request.session.get('group'):
        if 'School_Owner' in [i for i in request.session.get('group')]:
            return redirect('school:school_profile')
        if 'School_Teacher' in [i for i in request.session.get('group')]:
            return redirect('teacher:teacher_profile')
        if 'Admin' in [i for i in request.session.get('group')]:
            school = []
            for i in School.objects.all():
                i.domain = [v for v in Domain.objects.all().filter(tenant = i)]
                school.append(i)
            context = {
                'schools' : school ,
            }
            return render(request ,'Main/Main.html',context)
        # if 'School_Student' in [i for i in request.session.get('group')]:
        #     return redirect('student:student_profile')
    site = request.META['HTTP_HOST'].split(":")[0]
    try:
        if "." in site:
            school = get_object_or_404(School , schema_name = site.split(".")[0])
            return redirect('school:school_profile')
    except:
        pass
    schools = []
    for i in School.objects.all():
        i.domain = [v for v in Domain.objects.all().filter(tenant = i)]
        schools.append(i)
    context = {
        'schools' : schools ,
    }
    return render(request ,'Main/Main.html',context)

def ManageLoginView(request):
    context = {
        'login' : True ,
    }
    return render(request ,'Main/Main.html',context)

def NotAuthorized(request):
    context = {
    }
    return render(request,'Includes/NotAuthorized.html',context)

def PageNotFound(request,exception=None):
    context = {
    }
    return render(request,'Includes/404.html',context)

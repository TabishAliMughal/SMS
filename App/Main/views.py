from django.shortcuts import get_object_or_404, render , redirect
from tenant_schemas.utils import tenant_context
from School.S_School.models import School , Domain
from School.S_Students.models import Student
from School.S_Teachers.models import Teacher
from django.http import StreamingHttpResponse


def ManageMainPageView(request,rejected=None):
    if request.user.is_authenticated and request.session.get('group'):
        if 'School_Teacher' in [i for i in request.session.get('group')]:
            return redirect('teacher:teacher_profile')
        if 'School_Student' in [i for i in request.session.get('group')]:
            return redirect('student:student_profile')
    site = request.META['HTTP_HOST']
    try:
        if "." in site:
            get_object_or_404(School , schema_name = site.split(".")[0])
            if rejected :
                return redirect('school:school_profile',"rejected")
            else:
                return redirect('school:school_profile')
    except:
        pass
    schools = []
    for i in School.objects.all():
        i.domain = [v for v in Domain.objects.all().filter(tenant = i)]
        teachers = []
        students = []
        if i.schema_name != 'public':
            with tenant_context(i):
                for p in Teacher.objects.all().filter(active = True):
                    teachers.append(p)
                for p in Student.objects.all().filter(active = True):
                    students.append(p)
            i.teachers = { 'teachers' : teachers , 'count' : len(teachers) }
            i.students = { 'students' : students , 'count' : len(students) }
            schools.append(i)
    context = {
        'schools' : schools ,
    }
    if rejected:
        context['message'] = "User Not Found"
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



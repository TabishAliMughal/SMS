from django.shortcuts import get_object_or_404, render
from School.S_Record.models import ClassSubjects
from School.S_Students.models import Student , StudentStatus
from School.S_Teachers.models import Teacher
from Teacher.T_Teachers.views import get_teacher
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

def get_students(request):
    students = []
    for j in Student.objects.all().filter(active = "True").order_by('gr_number'):
        try:
            status = get_object_or_404(StudentStatus , student = j , valid = "True")
            j.status = status
            for k in get_object_or_404(ClassSubjects,clas = j.status.current_section.clas).subject.all():
                if k.pk in [ l.pk for l in get_teacher(request).subjects.subjects.all()]:
                    if j not in students:
                        students.append(j)
        except:
            pass
    return students

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherClassStudentsList(request):
    teacher = get_teacher(request)
    students = get_students(request)
    context = {
        'teacher' : teacher ,
        'students' : students ,
    }
    return render(request ,'T_Student/List.html',context)

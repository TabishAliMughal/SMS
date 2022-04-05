from django.shortcuts import get_object_or_404, render
from School.S_Students.models import Student , StudentStatus
from School.S_Teachers.models import Teacher , TeacherClass , TeacherSalary , TeacherSubject
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required

def get_teacher(request):
    teacher = get_object_or_404(Teacher , user = request.user)
    teacher.clas = get_object_or_404(TeacherClass , teacher = teacher , valid = 'True')
    teacher.salary = get_object_or_404(TeacherSalary , teacher = teacher , valid = 'True')
    teacher.subjects = get_object_or_404(TeacherSubject , teacher = teacher , valid = 'True')
    return teacher

def get_students(teacher):
    students = []
    for j in Student.objects.all().filter(active = "True").order_by('gr_number'):
        try:
            status = get_object_or_404(StudentStatus , student = j , valid = "True")
            j.status = status
            students.append(j)
        except:
            pass
    return students

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Teacher'])
def ManageTeacherClassStudentsList(request):
    teacher = get_teacher(request)
    students = get_students(teacher)
    context = {
        'teacher' : teacher ,
        'students' : students ,
    }
    return render(request ,'T_Student/List.html',context)
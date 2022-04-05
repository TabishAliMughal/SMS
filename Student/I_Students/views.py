from django.shortcuts import get_object_or_404, render
from School.S_Students.models import Student, StudentStatus
from App.Authentication.user_handeling import allowed_users
from django.contrib.auth.decorators import login_required


def get_student(request):
    student = get_object_or_404(Student , user = request.user)
    student.current_class = get_object_or_404(StudentStatus , student = student).current_class
    student.current_section = get_object_or_404(StudentStatus , student = student).current_section
    student.current_session = get_object_or_404(StudentStatus , student = student).current_session
    return student

@login_required(login_url='main:login')
@allowed_users(allowed_roles=['School_Student'])
def ManageStudentProfileView(request):
    context = {

    }
    return render(request , 'I_Student/Profile.html',context)
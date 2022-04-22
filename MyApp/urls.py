from argparse import Namespace
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('', include("App.Main.urls" , namespace="main")),
    path('adminsite/', admin.site.urls),
    path('admin/', include("App.Authentication.urls" , namespace="auth")),
    # School
    path('school/', include("School.S_School.urls" , namespace="school")),
    path('school/record/', include("School.S_Record.urls" , namespace="school_record")),
    path('school/student/', include("School.S_Students.urls" , namespace="school_student")),
    path('school/teacher/', include("School.S_Teachers.urls" , namespace="school_teacher")),
    path('school/fee/', include("School.S_Fee.urls" , namespace="school_fee")),
    # Teacher
    path('teacher/', include("Teacher.T_Teachers.urls" , namespace="teacher")),
    path('teacher/student/', include("Teacher.T_Students.urls" , namespace="teacher_student")),
    path('teacher/homework/', include("Teacher.T_Homework.urls" , namespace="teacher_homework")),
    # Student
    path('student/', include("Student.I_Students.urls" , namespace="student")),
    path('student/homework/', include("Student.I_Homework.urls" , namespace="student_homework")),
    # Fee
    path('student/fee/', include("School.S_Fee.urls" , namespace="student_fee")),
]

handler404 = "App.Main.views.PageNotFound"
handler500 = "App.Main.views.PageNotFound"
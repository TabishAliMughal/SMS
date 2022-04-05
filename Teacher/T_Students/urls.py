from django.urls import path
from . import views

app_name = 'Students'

urlpatterns = [
    path('list/',views.ManageTeacherClassStudentsList , name='student_list'),
]
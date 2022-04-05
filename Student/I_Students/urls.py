from unicodedata import name
from django.urls import path
from . import views

app_name = 'Students'

urlpatterns = [
    path('profile/',views.ManageStudentProfileView , name = 'student_profile'),
]
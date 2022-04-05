from django.urls import path
from . import views

app_name = 'Teachers'

urlpatterns = [
    path('profile/',views.ManageTeacherProfileView , name='teacher_profile'),
]
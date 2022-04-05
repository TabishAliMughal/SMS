from unicodedata import name
from django.urls import path
from . import views

app_name = 'Homework'

urlpatterns = [
    path('list/',views.ManageStudentHomeworkList , name='homework_list'),
    path('detail/<pk>',views.ManageStudentHomeworkDetail , name='homework_detail'),
    path('start/<pk>',views.ManageStudentHomeworkStart , name='homework_start'),
    path('complete/<pk>',views.ManageStudentHomeworkComplete , name='homework_complete'),
]
from django.urls import path
from . import views

app_name = 'Teachers'

urlpatterns = [
    path('list/',views.ManageTeacherClassHomeworklList , name='homework_list'),
    path('create/',views.ManageTeacherClassHomeworklCreate , name='homework_create'),
    path('detail/<pk>',views.ManageTeacherClassHomeworklDetail , name='homework_detail'),
]
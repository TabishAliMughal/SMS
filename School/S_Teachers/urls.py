from django.urls import path
from . import views

app_name = 'Teachers'

urlpatterns = [
    path('list/',views.ManageTeachersListView , name = 'teacher_list'),
    path('edit/<pk>',views.ManageTeacherCreateView , name = 'teacher_edit'),
    path('create/',views.ManageTeacherCreateView , name = 'teacher_create'),
    path('class/<pk>',views.ManageTeacherClassCreateView , name = 'teacher_class'),
    path('history/<pk>',views.ManageTeacherHistoryView , name = 'teacher_history'),
    path('salary/<pk>',views.ManageTeacherSalaryCreateView , name = 'teacher_salary'),
    path('subject/<pk>',views.ManageTeacherSubjectCreateView , name = 'teacher_subject'),
    path('user/<pk>',views.ManageSchoolTeacherManageUserView , name = 'teacher_user_handle'),
]
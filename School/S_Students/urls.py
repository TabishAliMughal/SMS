from django.urls import path
from . import views

app_name = 'Students'

urlpatterns = [

    # Student
    path('add/',views.ManageStudentCreateView,name='student_create'),
    path('edit/<pk>',views.ManageStudentCreateView,name='student_edit'),
    path('list/',views.ManageSchoolStudentsListView,name='student_list'),
    path('history/<pk>',views.ManageSchoolStudentHistoryView,name='student_history'),
    path('user/<pk>',views.ManageSchoolStudentManageUserView,name='student_user_handle'),
    path('transfer/<pk>',views.ManageSchoolStudentTransferView,name='student_transfer'),
    path('user/qr/<pk>',views.ManageSchoolStudentQRGenerateView,name='student_id_qr'),
]
from unicodedata import name
from django.urls import path
from . import views

app_name = 'Record'

urlpatterns = [
    path('gr-register/',views.ManageSchoolGrRegisterView,name='gr_register'),
    # Class
    path('class/list',views.ManageClassListView,name='class_list'),
    path('class/create',views.ManageClassCreateView,name='class_create'),
    path('class/edit/<pk>',views.ManageClassCreateView,name='class_edit'),

    # Session
    path('session/list',views.ManageSessionListView,name='session_list'),
    path('session/create',views.ManageSessionCreateView,name='session_create'),
    path('session/edit/<pk>',views.ManageSessionCreateView,name='session_edit'),

    # Class Session
    path('class-section/list/<pk>',views.ManageClassSectionListView,name='class_section_list'),
    path('class-section/create/<clas>',views.ManageClassSectionCreateView,name='class_section_create'),
    path('class-section/edit/<pk>',views.ManageClassSectionCreateView,name='class_section_edit'),

    # Subject
    path('subject/list',views.ManageSubjectListView,name='subject_list'),
    path('subject/create',views.ManageSubjectCreateView,name='subject_create'),
    path('subject/edit/<pk>',views.ManageSubjectCreateView,name='subject_edit'),

    # Class Subject
    path('class-subject/list',views.ManageClassSubjectListView,name='class_subject_list'),
    path('class-subject/create',views.ManageClassSubjectCreateView,name='class_subject_create'),
    path('class-subject/edit/<pk>',views.ManageClassSubjectCreateView,name='class_subject_edit'),

    
    

]
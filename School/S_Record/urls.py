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

    # School Detail
    path('detail/',views.ManageSchoolDetailListView , name = 'detail_list'),
    path('detail/add/',views.ManageSchoolDetailCreateView , name = 'detail_create'),
    path('detail/edit/<pk>/',views.ManageSchoolDetailCreateView , name = 'detail_edit'),
    path('detail/change-status/<pk>/',views.ManageSchoolDetailChangeStatusView , name = 'detail_change_status'),

    # School Images
    path('album/images/',views.ManageSchoolAlbumImagesListView , name = 'album_images_list'),
    path('album/images/add/',views.ManageSchoolAlbumImagesCreateView , name = 'album_images_create'),
    path('album/images/edit/<pk>/',views.ManageSchoolAlbumImagesCreateView , name = 'album_images_edit'),
    path('album/images/change-status/<pk>/',views.ManageSchoolAlbumImagesChangeStatusView , name = 'album_images_change_status'),

    # School Videos
    path('album/videos/',views.ManageSchoolAlbumVideosListView , name = 'album_videos_list'),
    path('album/videos/add/',views.ManageSchoolAlbumVideosCreateView , name = 'album_videos_create'),
    path('album/videos/edit/<pk>/',views.ManageSchoolAlbumVideosCreateView , name = 'album_videos_edit'),
    path('album/videos/change-status/<pk>/',views.ManageSchoolAlbumVideosChangeStatusView , name = 'album_videos_change_status'),

    # School Announcements
    path('announcements/',views.ManageSchoolAnnouncementsListView , name = 'announcements_list'),
    path('announcements/add/',views.ManageSchoolAnnouncementsCreateView , name = 'announcements_create'),
    path('announcements/edit/<pk>/',views.ManageSchoolAnnouncementsCreateView , name = 'announcements_edit'),
    path('announcements/change-status/<pk>/',views.ManageSchoolAnnouncementsChangeStatusView , name = 'announcements_change_status'),

    # School Fee Structure
    path('fee-structure/',views.ManageSchoolFeeStructureListView , name = 'fee_structure_list'),
    path('fee-structure/add/',views.ManageSchoolFeeStructureCreateView , name = 'fee_structure_create'),
    path('fee-structure/edit/<pk>/',views.ManageSchoolFeeStructureCreateView , name = 'fee_structure_edit'),
    path('fee-structure/change-status/<pk>/',views.ManageSchoolFeeStructureChangeStatusView , name = 'fee_structure_change_status'),
    

]
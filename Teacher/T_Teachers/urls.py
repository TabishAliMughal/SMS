from django.urls import path
from . import views

app_name = 'Teachers'

urlpatterns = [
    path('profile/',views.ManageTeacherProfileView , name='teacher_profile'),
    
    # Teacher Detail
    path('detail/',views.ManageTeacherDetailListView , name = 'detail_list'),
    path('detail/add/',views.ManageTeacherDetailCreateView , name = 'detail_create'),
    path('detail/edit/<pk>/',views.ManageTeacherDetailCreateView , name = 'detail_edit'),
    path('detail/change-status/<pk>/',views.ManageTeacherDetailChangeStatusView , name = 'detail_change_status'),

    # Teacher Images
    path('album/images/',views.ManageTeacherAlbumImagesListView , name = 'album_images_list'),
    path('album/images/add/',views.ManageTeacherAlbumImagesCreateView , name = 'album_images_create'),
    path('album/images/edit/<pk>/',views.ManageTeacherAlbumImagesCreateView , name = 'album_images_edit'),
    path('album/images/change-status/<pk>/',views.ManageTeacherAlbumImagesChangeStatusView , name = 'album_images_change_status'),

    # Teacher Videos
    path('album/videos/',views.ManageTeacherAlbumVideosListView , name = 'album_videos_list'),
    path('album/videos/add/',views.ManageTeacherAlbumVideosCreateView , name = 'album_videos_create'),
    path('album/videos/edit/<pk>/',views.ManageTeacherAlbumVideosCreateView , name = 'album_videos_edit'),
    path('album/videos/change-status/<pk>/',views.ManageTeacherAlbumVideosChangeStatusView , name = 'album_videos_change_status'),

]
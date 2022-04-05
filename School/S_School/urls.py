from unicodedata import name
from django.urls import path
from . import views

app_name = 'School'

urlpatterns = [
    path('',views.ManageSchoolProfileView , name = 'school_profile'),
    path('add/',views.ManageSchoolCreateView , name = 'create_school')
]
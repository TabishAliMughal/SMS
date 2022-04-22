from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('',views.ManageMainPageView , name='main'),
    path('rejected/<rejected>/',views.ManageMainPageView , name='main'),
    path('login/',views.ManageLoginView , name='login'),
    path('not-authorized/', views.NotAuthorized, name='not_authorized'),
]
from django.urls import path
from . import views

app_name = 'Attendance'

urlpatterns = [
    path('attendance/',views.ManageTeacherAttendanceView , name='teacher_attendance'),
    path('attendance/capture/',views.ManageTeacherAttendanceCaptureView , name='teacher_capture_attendance'),

]
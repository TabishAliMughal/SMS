from django.urls import path
from . import views

app_name = 'Attendance'

urlpatterns = [
    path('attendance/',views.ManageStudentAttendanceView , name='student_attendance'),
    path('attendance/via-date',views.ManageStudentAttendanceViaDateView , name='student_attendance_via_date'),
    path('attendance/via-class/<pk>',views.ManageStudentAttendanceViaClassView , name='student_attendance_via_class'),
    path('attendance/capture/',views.ManageStudentAttendanceCaptureView , name='student_capture_attendance'),

]
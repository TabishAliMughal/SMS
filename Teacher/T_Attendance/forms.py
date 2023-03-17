from django import forms
from Teacher.T_Attendance.models import TeacherAttendance


class ManageTeacherAttendanceCaptureForm(forms.ModelForm):
    class Meta:
        model = TeacherAttendance
        fields = [
            'teacher',
            'date_of_attendance',
            'capture_datetime',
        ]

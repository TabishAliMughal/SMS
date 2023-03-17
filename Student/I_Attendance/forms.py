from django import forms
from Student.I_Attendance.models import StudentAttendance


class ManageStudentAttendanceCaptureForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = [
            'student',
            'date_of_attendance',
            'capture_datetime',
        ]

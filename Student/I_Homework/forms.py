from django import forms
from .models import StudentHomeworkStatus

class ManageStudentHomeworkStatusCreateForm(forms.ModelForm):
    class Meta:
        model = StudentHomeworkStatus
        fields = [
            'student',
            'homework',
            'status',
        ]
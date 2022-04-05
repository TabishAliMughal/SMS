from django import forms
from .models import Student , StudentStatus

class ManageStudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'user',
            'gr_number',
            'name',
            'father_name',
            'address',
            'picture',
            'mobile1',
            'mobile2',
            'class_of_admission',
            'session_of_admission',
            'date_of_admission',
            'last_school',
            'religion',
            'gender',
            'date_of_birth',
            'active',
            'left_date',
            'reason_of_left',
            'remarks',
        ]


class ManageStudentStatusCreateForm(forms.ModelForm):
    class Meta:
        model = StudentStatus
        fields = [
            'student',
            'current_class',
            'current_section',
            'valid',
            'current_session',
        ]
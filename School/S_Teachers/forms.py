from django import forms
from .models import Teacher , TeacherClass , TeacherSalary , TeacherSubject

class ManageTeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'user',
            'name',
            'father_name',
            'address',
            'picture',
            'mobile1',
            'mobile2',
            'nic',
            'date_of_interview',
            'date_of_joining',
            'last_school',
            'religion',
            'gender',
            'date_of_birth',
            'active',
            'left_date',
            'reason_of_left',
            'remarks',
        ]

class ManageTeacherSalaryCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherSalary
        fields = [
            'teacher',
            'salary',
            'valid',
        ]

class ManageTeacherClassCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherClass
        fields = [
            'teacher',
            'clas',
            'valid',
        ]

class ManageTeacherSubjectCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherSubject
        fields = [
            'teacher',
            'subjects',
            'valid',
        ]

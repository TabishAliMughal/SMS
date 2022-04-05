from django import forms
from .models import Homework , HomeworkImage , HomeworkVideo

class ManageHomeworkCreateForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = [
            'teacher',
            'clas',
            'subject',
            'text',
            'date',
        ]

class ManageHomeworkImageCreateForm(forms.ModelForm):
    class Meta:
        model = HomeworkImage
        fields = [
            'homework',
            'image',
            'text',
        ]

class ManageHomeworkVideoCreateForm(forms.ModelForm):
    class Meta:
        model = HomeworkVideo
        fields = [
            'homework',
            'video',
            'text',
        ]

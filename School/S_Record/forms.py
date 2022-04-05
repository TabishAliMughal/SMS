from django import forms
from .models import ClassSection , Class, ClassSubjects , Session, Subject

class ManageClassCreateForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            'serial',
            'name'
        ]

class ManageSessionCreateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = [
            'serial',
            'name'
        ]

class ManageClassSectionCreateForm(forms.ModelForm):
    class Meta:
        model = ClassSection
        fields = [
            'serial',
            'name',
            'clas',
        ]

class ManageSubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'name',
        ]
class ManageClassSubjectCreateForm(forms.ModelForm):
    class Meta:
        model = ClassSubjects
        fields = [
            'subject',
            'clas',
        ]

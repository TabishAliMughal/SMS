from django import forms
from .models import ClassSection , Class, ClassSubjects , Session, Subject , SchoolDetail , SchoolAlbumImages , SchoolAlbumVideos , SchoolAnnouncements , SchoolFeeStructure

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

class ManageSchoolDetailCreateForm(forms.ModelForm):
    class Meta:
        model = SchoolDetail
        fields = [
            'detail',
            'valid',
        ]

class ManageSchoolAlbumImagesCreateForm(forms.ModelForm):
    class Meta:
        model = SchoolAlbumImages
        fields = [
            'image',
            'valid',
        ]

class ManageSchoolAlbumVideosCreateForm(forms.ModelForm):
    class Meta:
        model = SchoolAlbumVideos
        fields = [
            'url',
            'valid',
        ]

class ManageSchoolAnnouncementsCreateForm(forms.ModelForm):
    class Meta:
        model = SchoolAnnouncements
        fields = [
            'announcement',
            'valid',
        ]

class ManageSchoolFeeStructureCreateForm(forms.ModelForm):
    class Meta:
        model = SchoolFeeStructure
        fields = [
            'clas',
            'fee',
            'valid',
        ]

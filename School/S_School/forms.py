from django import forms
from .models import Domain, School


class ManageSchoolCreateForm(forms.ModelForm):
    class Meta:
        model = School
        fields = [
            'schema_name',
            'short_name',
            'address',
            'full_name',
            'mobile',
            'principal_name',
            'easypaisa',
            'logo',
            'active',
        ]

class ManageDomainCreateForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = [
            'domain',
            'tenant',
            'is_primary',
        ]
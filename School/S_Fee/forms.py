from django import forms

from School.S_Record.models import FeeTypes
from .models import StudentFeeRecord


class ManageFeeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = FeeTypes
        fields = [
            'name'
        ]


class ManageStudentFeeRecordCreateForm(forms.ModelForm):
    class Meta:
        model = StudentFeeRecord
        fields = [
            'student',
            'fee',
            'year',
            'month',
            'due_date',
            'status',
            'paid_amount',
            'paid_date',
        ]
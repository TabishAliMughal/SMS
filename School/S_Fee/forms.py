from django import forms
from .models import StudentFeeRecord

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
from django.db import models
from School.S_Students.views import Student , StudentFee
import calendar


class StudentFeeRecord(models.Model):
    student = models.ForeignKey(Student , on_delete=models.PROTECT)
    fee = models.ForeignKey(StudentFee , on_delete=models.PROTECT)
    MONTH_CHOICES = [(calendar.month_name[i] , calendar.month_name[i]) for i in range(1,13)]
    month = models.CharField(max_length=9, choices=MONTH_CHOICES)
    due_date = models.DateField()
    status_choices = (
        ("Paid",'Paid'),
        ("Due","Due"),
        ("PartialyPaid","PartialyPaid"),
    )
    status = models.CharField(choices=status_choices , max_length=15)
    year = models.IntegerField()
    paid_amount = models.IntegerField(blank=True , null = True)
    paid_date = models.DateTimeField(blank = True , null = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.name

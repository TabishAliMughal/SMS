from django.db import models
from School.S_Students.models import Student


class StudentAttendance(models.Model):
    student = models.ForeignKey(Student , on_delete=models.PROTECT)
    date_of_attendance = models.DateField()
    capture_datetime = models.DateTimeField()
    def __str__(self):
        return str(self.student)
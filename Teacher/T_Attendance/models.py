from django.db import models
from School.S_Teachers.models import Teacher


class TeacherAttendance(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.PROTECT)
    date_of_attendance = models.DateField()
    capture_datetime = models.DateTimeField()
    def __str__(self):
        return str(self.teacher)
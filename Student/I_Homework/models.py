from django.db import models
from School.S_Homework.models import Homework
from School.S_Students.models import Student


class StudentHomeworkStatus(models.Model):
    student = models.ForeignKey(Student , on_delete = models.PROTECT)
    homework = models.ForeignKey(Homework , on_delete = models.PROTECT)
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = (("student", "homework"))
    def __str__(self):
        return "{}>{}".format(self.student.name,self.homework)
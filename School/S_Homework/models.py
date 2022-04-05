from django.db import models
from School.S_Record.models import ClassSection, Subject
from School.S_Teachers.models import Teacher


class Homework(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.PROTECT)
    clas = models.ForeignKey(ClassSection , on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject , on_delete=models.PROTECT)
    text = models.CharField(max_length=500)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.date)

class HomeworkImage(models.Model):
    homework = models.ForeignKey(Homework , on_delete=models.PROTECT)
    image = models.FileField(upload_to="Homework/Images/")
    text = models.CharField(max_length=300 , blank=True , null=True)
    def __str__(self):
        return str(self.homework.date)
    
class HomeworkVideo(models.Model):
    homework = models.ForeignKey(Homework , on_delete=models.PROTECT)
    video = models.URLField()
    text = models.CharField(max_length=300 , blank=True , null=True)
    def __str__(self):
        return str(self.homework.date)
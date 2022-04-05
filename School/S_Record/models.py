from django.db import models
from django.contrib.auth.models import User
from School.S_School.models import School


class Class(models.Model):
    serial = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Session(models.Model):
    serial = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ClassSection(models.Model):
    serial = models.IntegerField()
    clas = models.ForeignKey(Class,on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    def __str__(self):
        return "{} > {}".format(self.clas.name,self.name)
    class Meta:
        unique_together = (("serial", "clas"))

class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ClassSubjects(models.Model):
    subject = models.ManyToManyField(Subject)
    clas = models.ForeignKey(Class , on_delete=models.PROTECT)
    def __str__(self):
        return self.clas.name
from django.db import models
from School.S_School.models import School
from django.contrib.auth.models import User
from School.S_Record.models import Class, Subject

class Teacher(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT , blank=True , null= True)
    password = models.CharField(max_length=50,blank=True,null=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    picture = models.FileField(blank=True , null=True,upload_to="Teacher/Pictures/")
    mobile1 = models.BigIntegerField()
    mobile2 = models.BigIntegerField(blank=True , null=True)
    nic = models.BigIntegerField(blank=True , null=True)
    date_of_interview = models.DateField()
    date_of_joining = models.DateField(blank=True , null=True)
    last_school = models.ForeignKey(School,on_delete=models.PROTECT,blank=True , null=True)
    religion_choices = (
        ('Islam',"Islam"),
        ('Christianity',"Christianity"),
        ('Other',"Other")
    )
    religion = models.CharField(max_length=50 , choices=religion_choices)
    gender_choices = (
        ('Male',"Male"),
        ('Female',"Female"),
        ('Other',"Other")
    )
    gender = models.CharField(max_length=50 , choices=gender_choices)
    date_of_birth = models.DateField(blank=True , null=True)
    active = models.BooleanField()
    left_date = models.DateField(blank=True , null=True)
    reason_of_left = models.CharField(max_length=500 , blank=True , null=True)
    remarks = models.CharField(max_length=500 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class TeacherSalary(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.PROTECT)
    salary = models.IntegerField()
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.salary)

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.PROTECT)
    clas = models.ForeignKey(Class , on_delete=models.PROTECT)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.clas.name

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher , on_delete=models.PROTECT)
    subjects = models.ManyToManyField(Subject)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




from django.db import models
from School.S_Record.models import Class , ClassSection , Session , FeeTypes
from django.contrib.auth.models import User
from School.S_School.models import School



class Student(models.Model):
    user = models.OneToOneField(User , on_delete=models.PROTECT , blank=True , null= True)
    password = models.CharField(max_length=30, blank=True , null= True)
    gr_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    picture = models.FileField(blank=True , null=True,upload_to="Students/Pictures/")
    mobile1 = models.BigIntegerField()
    mobile2 = models.BigIntegerField(blank=True , null=True)
    class_of_admission = models.ForeignKey(Class , on_delete=models.PROTECT)
    session_of_admission = models.ForeignKey(Session , on_delete=models.PROTECT)
    date_of_admission = models.DateField()
    last_school = models.ForeignKey(School,related_name="LastSchool",on_delete=models.PROTECT,blank=True , null=True)
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
    date_of_birth = models.DateField()
    active = models.BooleanField()
    left_date = models.DateField(blank=True , null=True)
    reason_of_left = models.CharField(max_length=500 , blank=True , null=True)
    remarks = models.CharField(max_length=500 , blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class StudentStatus(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    current_class = models.ForeignKey(Class , on_delete=models.PROTECT)
    current_section = models.ForeignKey(ClassSection , on_delete=models.PROTECT)
    current_session = models.ForeignKey(Session , on_delete=models.PROTECT)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.name


class StudentFee(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT)
    fee_type = models.ForeignKey(FeeTypes , on_delete = models.PROTECT)
    fee = models.IntegerField()
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        if str(self.valid) == "True":
            return "{}>{}".format(self.student.name,self.fee_type)
        else:
            return str(self.fee)

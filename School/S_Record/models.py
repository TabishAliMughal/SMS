from django.db import models


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

class SchoolDetail(models.Model):
    detail = models.CharField(max_length=5000)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.detail

class SchoolAlbumImages(models.Model):
    image = models.FileField(upload_to="School/Album/")
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.image)

class SchoolAlbumVideos(models.Model):
    url = models.URLField()
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.url

class SchoolAnnouncements(models.Model):
    announcement = models.CharField(max_length=1000)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.announcement

class SchoolFeeStructure(models.Model):
    clas = models.ForeignKey(Class , on_delete=models.PROTECT)
    fee = models.CharField(max_length=1000)
    valid = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fee
    class Meta:
        unique_together = (("clas", "fee", "valid"))

class FeeTypes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
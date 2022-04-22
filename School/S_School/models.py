from django.db import models
from django_tenants.models import TenantMixin , DomainMixin
from School.S_Record.models import Class


class School(TenantMixin):
    short_name = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    full_name = models.CharField(max_length=100)
    mobile =  models.BigIntegerField()
    principal_name = models.CharField(max_length=50)
    easypaisa = models.BigIntegerField(blank=True,null=True)
    logo = models.FileField(blank=True,null=True,upload_to="School/Logo/")
    active = models.BooleanField()
    auto_create_schema = True
    auto_drop_schema = True
    def __str__(self):
        return self.full_name

class Domain(DomainMixin):
    pass

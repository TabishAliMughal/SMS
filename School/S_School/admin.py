from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from School.S_School.models import Domain, School


# class SchoolModel(admin.ModelAdmin):
#     list_display = ('short_name','principal_name')

# admin.site.register(School,SchoolModel)
# admin.site.register(Domain)

from django_tenants.admin import TenantAdminMixin

from .models import Domain, School


class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1

@admin.register(School)
class SchoolAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = (
        "short_name",
        "principal_name",
        "active",
    )
    inlines = [DomainInline]

admin.site.register(Domain , ImportExportModelAdmin)
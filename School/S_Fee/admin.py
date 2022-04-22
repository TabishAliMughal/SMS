from django.contrib import admin
from .models import StudentFeeRecord
from import_export.admin import ImportExportModelAdmin

class StudentFeeRecordModel(ImportExportModelAdmin):
    list_display = ['student','fee','month','status']
    list_filter = ['student','fee','month','status']

admin.site.register(StudentFeeRecord,StudentFeeRecordModel)
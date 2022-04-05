from django.contrib import admin
from .models import StudentHomeworkStatus
from import_export.admin import ImportExportModelAdmin



class StudentHomeworkStatusModels(ImportExportModelAdmin):
    list_display = ['student','homework','status']

admin.site.register(StudentHomeworkStatus,StudentHomeworkStatusModels)
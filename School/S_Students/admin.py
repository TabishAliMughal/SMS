from django.contrib import admin
from .models import Student , StudentStatus
from import_export.admin import ImportExportModelAdmin



class StudentStatusModel(admin.TabularInline):
    model = StudentStatus
    list_display = ('student','current_session','valid')

class StudentModel(ImportExportModelAdmin):
    list_display = ('gr_number','name')
    search_fields = ['gr_number','name','school']
    inlines = [StudentStatusModel]

class StudentStatusModels(ImportExportModelAdmin):
    list_display = ['student']

admin.site.register(StudentStatus,StudentStatusModels)

admin.site.register(Student,StudentModel)
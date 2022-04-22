from django.contrib import admin
from .models import Student , StudentStatus , StudentFee
from import_export.admin import ImportExportModelAdmin



class StudentStatusInline(admin.TabularInline):
    model = StudentStatus
    list_display = ('student','current_session','valid')
    max_num = 1

class StudentFeeInline(admin.TabularInline):
    model = StudentFee
    list_display = ('student','fee','valid')
    max_num = 1

class StudentModel(ImportExportModelAdmin):
    list_display = ('gr_number','name')
    search_fields = ['gr_number','name','school']
    inlines = [StudentStatusInline,StudentFeeInline]

class StudentStatusModel(ImportExportModelAdmin):
    search_fields = ['student','current_class','valid']
    list_display = ['student','current_class','valid']

class StudentFeeModel(ImportExportModelAdmin):
    search_fields = ['student','fee','valid']
    list_display = ['student','fee','valid']

admin.site.register(StudentFee,StudentFeeModel)
admin.site.register(StudentStatus,StudentStatusModel)
admin.site.register(Student,StudentModel)
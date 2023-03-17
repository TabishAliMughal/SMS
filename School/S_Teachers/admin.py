from django.contrib import admin
from .models import Teacher , TeacherClass , TeacherSalary , TeacherSubject
from import_export.admin import ImportExportModelAdmin

class TeacherModel(ImportExportModelAdmin):
    list_display = ('name','mobile1')
    search_fields = ['name','mobile1','school']

admin.site.register(Teacher,TeacherModel)

class TeacherSalaryModel(ImportExportModelAdmin):
    list_display = ('teacher','salary')
    search_fields = ['teachr','salary']

admin.site.register(TeacherSalary,TeacherSalaryModel)

class TeacherClassModel(ImportExportModelAdmin):
    list_display = ('teacher','clas')
    search_fields = ['teachr','clas']

admin.site.register(TeacherClass,TeacherClassModel)

class TeacherSubjectModel(ImportExportModelAdmin):
    list_display = ('teacher','get_subjects')
    search_fields = ['teacher','subjects']

admin.site.register(TeacherSubject,TeacherSubjectModel)
from django.contrib import admin
from School.S_Record.models import ClassSection, ClassSubjects, Session, Class, Subject
from import_export.admin import ImportExportModelAdmin



class ClassModel(ImportExportModelAdmin):
    list_display = ('serial','name')
    search_fields = ['serial','name']

class SessionModel(ImportExportModelAdmin):
    list_display = ('serial','name')

class ClassSectionModel(ImportExportModelAdmin):
    list_display = ('serial','name','clas')

class SubjectModel(ImportExportModelAdmin):
    pass

class ClassSubjectModel(ImportExportModelAdmin):
    pass

admin.site.register(Class,ClassModel)
admin.site.register(Session,SessionModel)
admin.site.register(ClassSection,ClassSectionModel)
admin.site.register(Subject,SubjectModel)
admin.site.register(ClassSubjects,ClassSubjectModel)
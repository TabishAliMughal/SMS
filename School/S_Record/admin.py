from django.contrib import admin
from School.S_Record.models import ClassSection, ClassSubjects, Session, Class, Subject , SchoolDetail , SchoolAlbumImages , SchoolAlbumVideos , SchoolAnnouncements , SchoolFeeStructure , FeeTypes
from import_export.admin import ImportExportModelAdmin

class FeeTypesModel(ImportExportModelAdmin):
    list_display = ['name']

admin.site.register(FeeTypes,FeeTypesModel)


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

class SchoolDetailModel(ImportExportModelAdmin):
    list_display = ('detail','valid')

class SchoolAlbumImagesModel(ImportExportModelAdmin):
    pass

class SchoolAlbumVideosModel(ImportExportModelAdmin):
    list_display = ('url','valid')

class SchoolAnnouncementsModel(ImportExportModelAdmin):
    list_display = ('announcement','valid')

class SchoolFeeStructureModel(ImportExportModelAdmin):
    list_display = ('clas','fee','valid')

admin.site.register(Class,ClassModel)
admin.site.register(Session,SessionModel)
admin.site.register(ClassSection,ClassSectionModel)
admin.site.register(Subject,SubjectModel)
admin.site.register(ClassSubjects,ClassSubjectModel)
admin.site.register(SchoolDetail,SchoolDetailModel)
admin.site.register(SchoolAlbumImages,SchoolAlbumImagesModel)
admin.site.register(SchoolAlbumVideos,SchoolAlbumVideosModel)
admin.site.register(SchoolAnnouncements,SchoolAnnouncementsModel)
admin.site.register(SchoolFeeStructure,SchoolFeeStructureModel)
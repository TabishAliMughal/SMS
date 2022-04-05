from django.contrib import admin
from .models import Homework , HomeworkImage , HomeworkVideo
from import_export.admin import ImportExportModelAdmin

class HomeworkImageInline(admin.TabularInline):
    model = HomeworkImage
    max_num = 1

class HomeworkVideoInline(admin.TabularInline):
    model = HomeworkVideo

class HomeworkImageModel(ImportExportModelAdmin):
    pass

class HomeworkVideoModel(ImportExportModelAdmin):
    pass

class HomeworkModel(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('teacher','clas','subject','date')
    search_fields = ['teacher','clas','subject','date']
    inlines = [HomeworkImageInline,HomeworkVideoInline]


admin.site.register(Homework,HomeworkModel)
admin.site.register(HomeworkImage,HomeworkImageModel)
admin.site.register(HomeworkVideo,HomeworkVideoModel)
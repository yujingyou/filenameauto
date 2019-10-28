from django.contrib import admin

# Register your models here.
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import InMemoryUploadedFile

from filenameauto.settings import MEDIA_ROOT
from name_generate.models import *
from name_generate.utils import ImportDatabase
import os


class ProjectClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = (u'flieclass',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    list_filter = (u'project',)


class SchemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    list_filter = (u'project',)


class TechniFileNameAdmin(admin.ModelAdmin):
    list_display = ('result', 'project', 'scheme', 'module', 'name', 'author')
    list_filter = (u'project', u'name', u'author')


class PlanFileNameAdmin(admin.ModelAdmin):
    list_display = ('result', 'project', 'phase', 'name', 'author', 'date')
    list_filter = (u'project', u'name', u'author')


class RecordFileNameAdmin(admin.ModelAdmin):
    list_display = ('result', 'project', 'name', 'author', 'date')
    list_filter = (u'project', u'name', u'author')


class ImportFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'datetime')
    readonly_fields = ('datetime',)

    def save_model(self, request, obj, form, change):

        re = super().save_model(request, obj, form, change)
        data = request.FILES.get("file", None)
        if data is None:
            return re
        path = u'tmp/excel'
        allPath = MEDIA_ROOT + '/' + path
        print(allPath)
        if os.path.exists(allPath):
            os.remove(allPath)
        path = default_storage.save(path, data)
        ImportDatabase(allPath)
        return re


admin.site.register(FlieClass)
admin.site.register(ProjectFlieClass, ProjectClassAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(TechniFileName, TechniFileNameAdmin)
admin.site.register(PlanFileName, PlanFileNameAdmin)
admin.site.register(RecordFileName, RecordFileNameAdmin)
admin.site.register(ImportFile, ImportFileAdmin)
admin.site.site_title = "项目文件名自动生成后台数据库"
admin.site.site_header = "项目文件名后台数据管理"

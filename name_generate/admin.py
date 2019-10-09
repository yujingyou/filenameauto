from django.contrib import admin

# Register your models here.
from name_generate.models import *


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


admin.site.register(FlieClass)
admin.site.register(ProjectFlieClass, ProjectClassAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(TechniFileName, TechniFileNameAdmin)
admin.site.register(PlanFileName, PlanFileNameAdmin)
admin.site.register(RecordFileName, RecordFileNameAdmin)

admin.site.site_title = "项目文件名自动生成后台数据库"
admin.site.site_header = "项目文件名后台数据管理"

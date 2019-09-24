from django.contrib import admin

# Register your models here.
from name_generate.models import *

admin.site.register(FlieClass)
admin.site.register(ProjectClass)
admin.site.register(Project)
admin.site.register(FileName)
from re import search
from django.contrib import admin
from . import models
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title','description','technology','image','link')
    list_filter=('title', )
    ordering=('title', )
    search_field=('title')
admin.site.register(models.Project, ProjectAdmin)

class SkillsAdmin(admin.ModelAdmin):
    list_display=('name', )
    extra=2
admin.site.register(models.Skills, SkillsAdmin)


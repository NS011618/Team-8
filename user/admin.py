from django.contrib import admin
from user.models import course
# Register your models here.
class CAdmin(admin.ModelAdmin):
    list_display=['Name','Description','Objectives','Outcomes','Cost']
admin.site.register(course,CAdmin)
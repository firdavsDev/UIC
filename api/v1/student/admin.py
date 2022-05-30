from django.contrib import admin

# Register your models here.
from . import models

#import export
from import_export.admin import ImportExportActionModelAdmin



@admin.register(models.Student)
class StudentrAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number','otm', 'total_allocated_amount','contract_amount',]
    list_filter = ['full_name']
    list_display_links = ('id', 'full_name', 'phone_number')


@admin.register(models.OTM)
class OTMAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name',]
    list_filter = ['name']
    list_display_links = ('id', 'name')

admin.site.site_header = "Metsenat Admin Panel"
admin.site.site_title = "Metsenat API"
admin.site.index_title = "Metsenat API"
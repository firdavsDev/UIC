from django.contrib import admin

# Register your models here.
from . import models
#remove group
from django.contrib.auth.models import Group
admin.site.unregister(Group)

#import export
from import_export.admin import ImportExportActionModelAdmin

@admin.register(models.Sponsor)
class SponsorAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number','company_name','status','created_at' ]
    list_filter = ['status',]
    list_display_links = ('id', 'full_name', 'phone_number')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

@admin.register(models.SponsorAllocateAmount)
class SponsorAllocateAmounAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor', 'amount', 'created_at']
    list_display_links = ('id', 'sponsor', 'amount')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
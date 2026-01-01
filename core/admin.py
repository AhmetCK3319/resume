from django.contrib import admin
from core.models import *
# Register your models here.


class GeneralSettingAdmin(admin.ModelAdmin):

    list_display = ('name','description','parameters','updated_at','created_at')
    search_fields = ('name','description','parameters')
    list_editable = ('description','parameters')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25
    #prepopulated_fields = {'slug': ('site_name',)} slug alanları otomatik olarak doldurulur.

    class Meta:
        model = GeneralSetting

admin.site.register(GeneralSetting, GeneralSettingAdmin)

class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at', 'created_at')
    search_fields = ('name', 'description',)
    list_editable = ('description',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = ImageSetting

admin.site.register(ImageSetting, ImageSettingAdmin)
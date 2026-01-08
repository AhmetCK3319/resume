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


class SkillSettingAdmin(admin.ModelAdmin):
    list_display = ('id','name','order','persentage', 'description', 'updated_at', 'created_at')
    search_fields = ('name', 'description',)
    list_editable = ('name','order','persentage')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = SkillSetting

admin.site.register(SkillSetting, SkillSettingAdmin)



class ExperianceSettingAdmin(admin.ModelAdmin):
    list_display = ('id','job_title','company_name', 'locaiton', 'updated_at', 'created_at')
    search_fields = ('job_title', 'locaiton',)
    list_editable = ('job_title', 'locaiton')
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = ExperianceSetting

admin.site.register(ExperianceSetting, ExperianceSettingAdmin)


class EducationSettingAdmin(admin.ModelAdmin):
    list_display = ('id','scholl_name', 'major','department', 'updated_at', 'created_at')
    search_fields = ('scholl_name', 'major','department',)
    list_editable = ('scholl_name', 'major','department',)
    ordering = ('-start_date',)
    date_hierarchy = 'start_date'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = EducationSetting

admin.site.register(EducationSetting, EducationSettingAdmin)


class SocialSettingAdmin(admin.ModelAdmin):
    list_display = ('id','link', 'icon', 'updated_at', 'created_at')
    search_fields = ('link', 'icon',)
    list_editable = ('link', 'icon',)
    ordering = ('-updated_at',)
    date_hierarchy = 'updated_at'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = SocialSetting

admin.site.register(SocialSetting, SocialSettingAdmin)
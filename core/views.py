from django.shortcuts import render
from .models import GeneralSetting, ImageSetting


def index(request):
    site_title=GeneralSetting.objects.get(name='site_title').parameters
    site_keywords=GeneralSetting.objects.get(name='site_keywords').parameters
    site_description=GeneralSetting.objects.get(name='site_description').parameters
    home_banner_name=GeneralSetting.objects.get(name='home_banner_name').parameters
    home_banner_description=GeneralSetting.objects.get(name='home_banner_description').parameters
    home_banner_title=GeneralSetting.objects.get(name='home_banner_title').parameters

    #Images
    home_banner_image=ImageSetting.objects.get(name='home_banner_image').file
    fav_icon = ImageSetting.objects.get(name='fav_icon').file
    header_logo = ImageSetting.objects.get(name='header_logo').file




    context = {'site_title': site_title,
               'site_keywords': site_keywords,
               'site_description': site_description,
               'home_banner_name': home_banner_name,
               'home_banner_description': home_banner_description,
               'home_banner_title': home_banner_title,
               'home_banner_image': home_banner_image,
               'fav_icon': fav_icon,
               'header_logo': header_logo,
               }
    return render(request, 'index.html',context)


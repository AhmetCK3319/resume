from django.shortcuts import render
from unicodedata import category

from .models import GeneralSetting, ImageSetting, SkillSetting, ExperianceSetting, EducationSetting, SocialSetting


# tüm sayfalarda kullanılması için context_processors'ta çağrılan fonksiyon...

def get_setting(key, MODEL=None, parameter_name=None):
    if not parameter_name:
        parameter_name = 'parameters'
    if not MODEL:
        MODEL = GeneralSetting
    general_setting = MODEL.objects.filter(name=key).first()
    if general_setting:
        return getattr(general_setting, parameter_name)
    else:
        return ''


def layout(request):
    site_title = get_setting('site_title')
    site_keywords = get_setting('site_keywords')
    site_description = get_setting('site_description')
    home_banner_name = get_setting('home_banner_name')
    home_banner_description = get_setting('home_banner_description')
    home_banner_title = get_setting('home_banner_title')
    about_myself_wellcome = get_setting('about_myself_wellcome')
    about_myself_footer = get_setting('about_myself_footer')
    home_banner_image = get_setting('home_banner_image', ImageSetting, 'file')
    fav_icon = get_setting('fav_icon', ImageSetting, 'file')
    header_logo = get_setting('header_logo', ImageSetting, 'file')
    # Blog Page İmages
    socials = SocialSetting.objects.all()

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_description': home_banner_description,
        'home_banner_title': home_banner_title,
        'home_banner_image': home_banner_image,
        'about_myself_wellcome': about_myself_wellcome,
        'about_myself_footer': about_myself_footer,
        'fav_icon': fav_icon,
        'header_logo': header_logo,
        'socials': socials,
    }
    return context


def index(request):
    skills = SkillSetting.objects.all()
    experiances = ExperianceSetting.objects.all()
    educations = EducationSetting.objects.all()

    context = {

        'skills': skills,
        'experiances': experiances,
        'educations': educations,

    }
    return render(request, 'index.html', context)

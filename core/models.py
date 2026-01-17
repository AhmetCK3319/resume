from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractBaseModel(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        verbose_name='Updated_at',
        help_text=''
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        verbose_name='Created_at',
        help_text=''
    )

    class Meta:
        abstract = True


# genel ayarlar modeli
class GeneralSetting(AbstractBaseModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text=''
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameters = models.TextField(
        default='',
        blank=True,
        verbose_name='Parameters',
        help_text=''
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'


# image ayarları modeli
class ImageSetting(AbstractBaseModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text=''
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    file = models.FileField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='File',
        upload_to='image/',
        help_text=''
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'


class SkillSetting(AbstractBaseModel):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text=''
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
    )
    persentage = models.IntegerField(
        default=50,
        verbose_name='Persentage',
        help_text='',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill Setting'
        verbose_name_plural = 'Skill Settings'
        ordering = ['order']


class ExperianceSetting(AbstractBaseModel):
    company_name = models.CharField(
        default='',
        max_length=255,
        verbose_name='Company Name',
        help_text=''
    )
    job_title = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Job Title',
        help_text=''
    )
    locaiton = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Location',
        help_text=''
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        verbose_name='End Date',
        blank=True,
        null=True,
        help_text=''
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Experiance Setting'
        verbose_name_plural = 'Experiance Settings'
        ordering = ['-start_date']


class EducationSetting(AbstractBaseModel):
    scholl_name = models.CharField(
        default='',
        max_length=255,
        verbose_name='scholl name',
        help_text=''
    )
    major = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='major',
        help_text=''
    )
    department = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='department',
        help_text=''
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        verbose_name='End Date',
        blank=True,
        null=True,
        help_text=''
    )

    def __str__(self):
        return self.scholl_name

    class Meta:
        verbose_name = 'Education Setting'
        verbose_name_plural = 'Education Settings'
        ordering = ['-start_date']


class SocialSetting(AbstractBaseModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order',
        help_text=''
    )
    link = models.URLField(
        default='',
        max_length=255,
        verbose_name='Link',
        help_text=''
    )
    icon = models.CharField(
        default='',
        max_length=255,
        verbose_name='Icon',
        help_text=''
    )
    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Social Setting'
        verbose_name_plural = 'Social Settings'
        ordering = ['-order']
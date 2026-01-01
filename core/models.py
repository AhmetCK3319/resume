from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Name',
        help_text = ''
    )
    description = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Description',
        help_text=''
    )
    parameters = models.CharField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='Parameters',
        help_text=''
    )
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'

class ImageSetting(models.Model):
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
    file=models.FileField(
        default='',
        max_length=255,
        blank=True,
        verbose_name='File',
        upload_to='images/',
        help_text=''

    )
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
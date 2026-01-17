from django.db import models
from core.models import AbstractBaseModel

class Message(AbstractBaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        help_text='',
        blank=True,
        default=''
    )
    email = models.EmailField(
        verbose_name='Email',
        help_text='',
        blank=True,
        default='',
        max_length=255,
    )
    subject = models.CharField(
        max_length=255,
        verbose_name='Subject',
        help_text='',
        blank=True,
        default=''
    )
    message = models.TextField(
        verbose_name='Message',
        help_text='',
        blank=True,
        default=''
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('-created_at',)

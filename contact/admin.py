from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email','subject','message', 'updated_at', 'created_at')
    search_fields = ('name', 'email','subject','message')
    list_editable = ('name', 'email','subject','message')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25

    class Meta:
        model = Message

admin.site.register(Message, MessageAdmin)

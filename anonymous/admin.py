from django.contrib import admin
from .models import Message
from django.contrib.admin import ModelAdmin
from .models import Message
from django.contrib.auth import get_user_model
# Register your models here.
user = get_user_model()
class CustomAdmin(ModelAdmin):
    list_display = ['text', 'customuser', 'created', 'updated']
admin.site.register(Message, CustomAdmin)

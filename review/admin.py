from django.contrib import admin
from .models import Review
from django.contrib.admin import ModelAdmin
# Register your models here.
class CustomAdmin(ModelAdmin):
    list_display = ['name', 'occupation', 'created']

admin.site.register(Review, CustomAdmin)
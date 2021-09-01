from auth_app.models import CustomUser
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from django.conf import settings
User = get_user_model()


class Message(models.Model):
    customuser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-id']

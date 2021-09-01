from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class CustomUser(AbstractUser):
    pass

    def get_absolute_url(self):
        
        return reverse('message', kwargs={'username': self.username})
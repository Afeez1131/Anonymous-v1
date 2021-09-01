from django.db import models

# Create your models here.


class Review(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=50)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.

class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='')
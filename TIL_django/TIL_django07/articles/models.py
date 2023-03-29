from django.db import models

# Create your models here.

class Article(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=3)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    title = models.CharField(max_length=80)
    updated_at = models.DateField(auto_now_add=True)
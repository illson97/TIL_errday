from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    movie = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='')

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
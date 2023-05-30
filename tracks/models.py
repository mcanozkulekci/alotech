from django.db import models

# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    preview_url = models.TextField()
    image_url = models.TextField()

    # Add more fields as needed
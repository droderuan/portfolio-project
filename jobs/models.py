from django.db import models

# Create your models here.
class Job(models.Model):
    image_height = 255
    image = models.ImageField(upload_to='images/', height_field='image_height')
    summary = models.CharField(max_length=200)
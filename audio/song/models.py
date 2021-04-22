from django.db import models
from django.utils import timezone


class Songs(models.Model):
    song=models.CharField(max_length=100 )
    duration=models.IntegerField(null=True)
    upload_time=models.DateTimeField(auto_now_add=True)


# Create your models here.
 
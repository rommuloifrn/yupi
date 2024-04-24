from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .youtube_api_bridge import APIHandler

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)

class Pin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    video_id = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    visible = models.BooleanField()
    
    def snippet(self):
        return APIHandler.get_video_info(self.video_id)
        
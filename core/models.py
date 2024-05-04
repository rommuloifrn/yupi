from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .youtube_api_bridge import APIHandler

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(max_length=100, blank=True)
    location = models.CharField(max_length=30, blank=True)
    
class VideoUnit(models.Model):
    youtube_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    published_at = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    

class Pin(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
    text = models.TextField(max_length=400)
    visible = models.BooleanField()
    
    video = models.ForeignKey(VideoUnit, null=False, on_delete=models.CASCADE)
    
    def snippet(self):
        return APIHandler.get_video_info(self.video_id)
    
    def __str__(self):
        return f"{self.user} - {self.video}"
    


    
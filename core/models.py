from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    url = models.CharField(max_length=200)
    text = models.TextField(max_length=400)
    visible = models.BooleanField()
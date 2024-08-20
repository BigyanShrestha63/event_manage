from django.contrib.auth.models import User
from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='uploads/profiles/', max_length=255, default='uploads/profiles/default.jpg', blank=True, null=True)
    bio = models.TextField()
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

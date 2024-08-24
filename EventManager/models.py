from django.contrib.auth.models import User
from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='uploads/profiles/', max_length=255, default='uploads/profiles/default.jpg', blank=True, null=True)
    profession = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField()
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

class TicketPurchase(models.Model):
    TICKET_TYPES = [
        ('standard-access', 'Standard Access'),
        ('pro-access', 'Pro Access'),
        ('premium-access', 'Premium Access'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.ticket_type}'
    
class GalleryImage(models.Model):
    title = models.CharField(max_length=100,blank="true")
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description if self.description else f"Image {self.id}"
    


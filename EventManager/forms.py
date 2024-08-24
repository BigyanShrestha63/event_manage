from django import forms
from .models import *

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = TicketPurchase
        fields = ['name', 'email', 'ticket_type']
        widgets = {
            'ticket_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

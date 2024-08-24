from django.contrib import admin
from .models import *

admin.site.register(Speaker)


@admin.register(TicketPurchase)
class TicketPurchaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'ticket_type', 'purchase_date')
    list_filter = ('ticket_type', 'purchase_date')
    search_fields = ('name', 'email')
    

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'uploaded_at')
    

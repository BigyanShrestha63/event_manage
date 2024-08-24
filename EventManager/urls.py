from django.urls import path
from EventManager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),   
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('speakers/', views.speakers, name="speakers"),
    path('speaker_details/<int:id>/', views.speaker_details, name="speaker_details"),
    path('venue/', views.venue, name="venue"),
    path('gallery/', views.gallery, name='gallery'),
    path('sponsors/', views.sponsors, name="sponsors"),
    path('schedule/', views.schedule, name="schedule"),
    path('buy_ticket/', views.buy_ticket, name="buy_ticket"),
    path('ticket/', views.ticket,name="ticket"),
    path('success/', views.success, name='success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

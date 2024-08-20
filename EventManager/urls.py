from django.urls import path
from EventManager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),   
    path('speaker_details/<int:id>/', views.speaker_details, name="speaker_details"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

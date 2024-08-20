from django.shortcuts import render, get_object_or_404
from .models import Speaker

def home(request):
    speakers = Speaker.objects.all()
    return render(request, 'home.html', {'speakers': speakers})

def speaker_details(request, id):
    speaker = get_object_or_404(Speaker, id=id)
    return render(request, 'speaker_details.html', {'speaker': speaker})

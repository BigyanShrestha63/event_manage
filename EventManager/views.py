from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def venue(request):
    return render(request, 'venue.html', {})

def gallery(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'gallery.html',{})
    else:
        form = GalleryImageForm()

    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'form': form, 'images': images})


def speakers(request):
    speakers = Speaker.objects.all()
    return render(request, 'speakers.html', {'speakers': speakers})

def schedule(request):
    return render(request, 'schedule.html', {})

def sponsors(request):
    return render(request, 'sponsors.html', {})


def speaker_details(request, id):
    speaker = get_object_or_404(Speaker, id=id)
    return render(request, 'speaker_details.html', {'speaker': speaker})

def ticket(request):
    return render(request, 'ticket.html', {})


def buy_ticket(request):
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'success.html',{})
    else:
        initial_ticket_type = request.GET.get('ticket_type', '')
        form = TicketPurchaseForm(initial={'ticket_type': initial_ticket_type})
    
    return render(request, 'buy_ticket.html', {'form': form})


def success(request):
    return render(request, 'success.html',{})







import os
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.flatpages.models import FlatPage

from .models import Announcement, Event, UsefulLink, CarouselItem

def home_view(request):
    announcements = Announcement.objects.all()
    about_text = FlatPage.objects.get(url='/about-us/').content
    contact_text = FlatPage.objects.get(url='/contact/').content

    return render(request, 'pages/home_page.html', {'announcements': announcements, 'about_text': about_text, 'contact_text': contact_text})

def announce_view(request):
    announcements = Announcement.objects.all()

    return render(request, 'pages/announce_page.html', {'announcements': announcements})

def events_view(request):
    events = Event.objects.all()

    return render(request, 'pages/events_page.html', {'events': events})

def useful_links_view(request):
    useful_links = UsefulLink.objects.all()

    return render(request, 'pages/useful_links_page.html', {'useful_links': useful_links})

def bergi_view(request):
    return redirect('https://e-bergi.com')

def yarisma_view(request):
    return redirect('https://yarisma.cclub.metu.edu.tr')

def tuzuk_view(request):
    return FileResponse(open('./static/docs/odtu_bilgisayar_toplulugu_tuzugu.pdf', 'rb'), content_type='application/pdf')

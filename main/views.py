# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

from .models import Announcement, Event, Option, UsefulLink

def home_view(request):
    announcements = Announcement.objects.all()
    about_text = Option.objects.get(name='about_text').value

    return render(request, 'pages/home_page.html', {'announcements': announcements, 'about_text': about_text})

def about_view(request):
    about_text = Option.objects.get(name='about_text').value

    return render(request, 'pages/about_page.html', {'about_text': about_text})

def announce_view(request):
    announcements = Announcement.objects.all()

    return render(request, 'pages/announce_page.html', {'announcements': announcements})

def events_view(request):
    events = Event.objects.all()

    return render(request, 'pages/events_page.html', {'events': events})

def contact_view(request):
    return render(request, 'pages/contact_page.html')

def bilisim_gunu_view(request):
    return render(request, 'pages/bilisim_gunu_page.html')

def useful_links_view(request):
    useful_links = UsefulLink.objects.all()

    return render(request, 'pages/useful_links_page.html', {'useful_links': useful_links})

def bergi_view(request):
    return redirect('https://e-bergi.com')

def yarisma_view(request):
    return redirect('https://yarisma.cclub.metu.edu.tr')

def tuzuk_view(request):
    return FileResponse(open('./static/docs/odtu_bilgisayar_toplulugu_tuzugu.pdf', 'rb'), content_type='application/pdf')
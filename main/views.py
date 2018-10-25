# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.staticfiles.templatetags.staticfiles import static

def home_view(request):
    return render(request, 'pages/home_page.html')

def about_view(request):
    return render(request, 'pages/about_page.html')

def announce_view(request):
    return render(request, 'pages/announce_page.html')

def events_view(request):
    return render(request, 'pages/events_page.html')

def contact_view(request):
    return render(request, 'pages/contact_page.html')

def bilisim_gunu_view(request):
    return render(request, 'pages/bilisim_gunu_page.html')

def bergi_view(request):
    return redirect('https://e-bergi.com')

def yarisma_view(request):
    return redirect('https://yarisma.cclub.metu.edu.tr')

def tuzuk_view(request):
    return FileResponse(open('./static/docs/odtu_bilgisayar_toplulugu_tuzugu.pdf', 'rb'), content_type='application/pdf')
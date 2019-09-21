from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from django.utils import translation

from .models import *

def flatpage_view(request, template, name, site):
    flatpage = get_object_or_404(FlatPage, name=name, site=site)

    if flatpage.redirect_link is not None and flatpage.redirect_link is not '': return redirect(flatpage.redirect_link)

    return render(request, template, {
        'flatpage': flatpage
    })

def main_error_view(request, *args, **argv):
    return render(request, 'main_site/pages/404.html')

def main_home_view(request):
    return render(request, 'main_site/pages/home_page.html', {
        'announcements': Announcement.objects.all(),
        'about_page': get_object_or_404(FlatPage ,name='about-us', site='main'),
        'contact_page': get_object_or_404(FlatPage ,name='contact', site='main'),
        'main_site_sponsors_page': FlatPage.objects.filter(site='main', name='sponsors').first()
    })

def main_announce_view(request):
    return render(request, 'main_site/pages/announce_page.html', {
        'announcements': Announcement.objects.all()
    })

def main_events_view(request):
    return render(request, 'main_site/pages/events_page.html', {
        'events': Event.objects.all(),
    })

def main_useful_links_view(request):
    return render(request, 'main_site/pages/useful_links_page.html', {
        'useful_links': UsefulLink.objects.all(),
    })

def main_tuzuk_view(request):
    return FileResponse(open('./static/docs/tuzuk.pdf', 'rb'), content_type='application/pdf')

def contest_error_view(request, *args, **argv):
    return render(request, 'contest_site/pages/404.html')

def contest_home_view(request):
    return render(request, 'contest_site/pages/home_page.html', {
        'home_page': get_object_or_404(FlatPage, name='home', site='contest'),
    })

def contest_faq_view(request):
    return render(request, 'contest_site/pages/faq_page.html', {
        'contest_rules': ContestRule.objects.all(),
        'contest_faq_items':ContestFAQItem.objects.all(),
        'contest_supported_languages': ContestSupportedLanguage.objects.all(),
    })

def toggle_lang(request):
    lang = 'tr' if translation.get_language() == 'en' else 'en'

    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    return redirect(request.GET.get('next', '/'))

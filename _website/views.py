from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from django.utils import translation

from .models import *

def flatpage_view(request, template, name, site):
    flatpage = get_object_or_404(FlatPage ,name=name, site=site)

    if flatpage.redirect_link is not None and flatpage.redirect_link is not '':
        return redirect(flatpage.redirect_link)

    return render(request, template, {'flatpage': flatpage})

def main_error_404_view(request, error):
    return render(request, 'main_site/pages/404.html')

def main_home_view(request):
    announcements = Announcement.objects.all()

    lang = translation.get_language()

    main_site_sponsors_page = FlatPage.objects.filter(site='main', name='sponsors')

    if len(main_site_sponsors_page) > 0: main_site_sponsors_page = main_site_sponsors_page[0]

    about_page = FlatPage.objects.get(name='about-us', site='main')
    contact_page = FlatPage.objects.get(name='contact', site='main')

    return render(request, 'main_site/pages/home_page.html', {'announcements': announcements, 'about_page': about_page, 'contact_page': contact_page, 'main_site_sponsors_page': main_site_sponsors_page})

def main_announce_redirect_view(request):
    return redirect('announce')

def main_announce_view(request):
    announcements = Announcement.objects.all()

    return render(request, 'main_site/pages/announce_page.html', {'announcements': announcements})

def main_events_view(request):
    events = Event.objects.all()

    return render(request, 'main_site/pages/events_page.html', {'events': events})

def main_useful_links_view(request):
    useful_links = UsefulLink.objects.all()

    return render(request, 'main_site/pages/useful_links_page.html', {'useful_links': useful_links})

def main_tuzuk_view(request):
    return FileResponse(open('./static/docs/odtu_bilgisayar_toplulugu_tuzugu.pdf', 'rb'), content_type='application/pdf')

def contest_error_404_view(request, error):
    return render(request, 'contest_site/pages/404.html')

def contest_home_view(request):
    home_page = FlatPage.objects.get(name='home', site='contest')

    return render(request, 'contest_site/pages/home_page.html', {'home_page': home_page})

def contest_faq_view(request):
    contest_rules = ContestRule.objects.all()
    contest_faq_items = ContestFAQItem.objects.all()

    contest_supported_languages = ContestSupportedLanguage.objects.all()

    return render(request, 'contest_site/pages/faq_page.html', {'contest_rules': contest_rules, 'contest_faq_items':contest_faq_items, 'contest_supported_languages': contest_supported_languages})

def toggle_lang(request):
    lang = translation.get_language()

    if lang == 'en':
        lang = 'tr'
    else:
        lang = 'en'

    translation.activate(lang)

    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    return redirect(request.GET.get('next', '/'))

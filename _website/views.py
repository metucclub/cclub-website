from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, FileResponse
from django.utils import translation

from .models import *

def generate_menu_context(request):
    site = get_object_or_404(Site, pk=request.site)
    menu_items = MenuItem.objects.filter(site__pk=request.site)

    sponsors = FlatPage.objects.filter(name='sponsors', site__pk=request.site).first()

    return {
        'site': site,
        'sponsors': sponsors,
        'menu_items': menu_items,
    }


def flatpage_view(request, name):
    flatpage = get_object_or_404(FlatPage, name=name, site__pk=request.site)

    carousel_items = CarouselItem.objects.filter(site__pk=request.site)

    return render(request, '__blank.html' if flatpage.blank_page else 'pages/flatpage.html', {
        **generate_menu_context(request),
        'carousel_items': carousel_items,
        'flatpage': flatpage,
    })


def home_view(request):
    carousel_items = CarouselItem.objects.filter(site__pk=request.site)

    about = FlatPage.objects.filter(name='about', site__pk=request.site).first()
    contact = FlatPage.objects.filter(name='contact', site__pk=request.site).first()

    announcements = Announcement.objects.filter(site__pk=request.site)

    return render(request, 'pages/home.html', {
        **generate_menu_context(request),
        'carousel_items': carousel_items,
        'announcements': announcements,
        'about': about,
        'contact': contact,
    })


def announcements_view(request):
    announcements = Announcement.objects.filter(site__pk=request.site)

    if len(announcements) == 0:
        raise Http404()

    return render(request, 'pages/announcements.html', {
        **generate_menu_context(request),
        'announcements': announcements,
    })


def events_view(request):
    events = Event.objects.filter(site__pk=request.site)

    if len(events) == 0:
        raise Http404()

    return render(request, 'pages/events.html', {
        **generate_menu_context(request),
        'events': events,
    })


def useful_links_view(request):
    useful_links = UsefulLink.objects.filter(site__pk=request.site)

    if len(useful_links) == 0:
        raise Http404()

    return render(request, 'pages/useful_links.html', {
        **generate_menu_context(request),
        'useful_links': useful_links,
    })


def faq_view(request):
    faq_items = FAQItem.objects.filter(site__pk=request.site)
    contest_rules = ContestRule.objects.filter(site__pk=request.site)
    contest_languages = ContestLanguage.objects.filter(site__pk=request.site)

    if len(faq_items) == 0 and len(contest_rules) == 0 and len(contest_languages) == 0:
        raise Http404()

    return render(request, 'pages/faq.html', {
        **generate_menu_context(request),
        'faq_items': faq_items,
        'contest_rules': contest_rules,
        'contest_languages': contest_languages,
    })


def toggle_lang(request):
    lang = 'tr' if translation.get_language() == 'en' else 'en'

    translation.activate(lang)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang

    return redirect(request.GET.get('next', '/'))

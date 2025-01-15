from django.urls import path
from django.shortcuts import redirect
from _website.views import *

def arsiv_redirect(request):
    return redirect('https://www.arsiv.cclub.metu.edu.tr')

urlpatterns = [
    path('', home_view, name='home'),
    path('toggle-lang/', toggle_lang, name='toggle_lang'),
    path('announcements/', announcements_view, name='announcements'),
    path('announcements/<int:id>/', announcement_view, name='announcement'),
    path('events/', events_view, name='events'),
    path('useful-links/', useful_links_view, name='useful_links'),
    path('faq/', faq_view, name='faq'),
    path('arsiv/', arsiv_redirect, name ='arsiv'), #arsiv redirect
    path('<path:name>/', flatpage_view)
]

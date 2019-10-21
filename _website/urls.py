from django.urls import path

from _website.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('toggle-lang/', toggle_lang, name='toggle_lang'),
    path('announcements/', announcements_view, name='announcements'),
    path('events/', events_view, name='events'),
    path('useful-links/', useful_links_view, name='useful_links'),
    path('faq/', faq_view, name='faq'),
    path('<path:name>/', flatpage_view)
]

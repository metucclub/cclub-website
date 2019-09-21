from django.urls import path, include
from django.views.static import serve as static_serve

from django.conf import settings
from django.contrib import admin

from _website.views import *

SITE = 'main'
TEMPLATE = 'main_site/__flatpage.html'

handler404 = '_website.views.main_error_view'
handler500 = '_website.views.main_error_view'

urlpatterns = [
    path('1gan/', admin.site.urls),

    path('', main_home_view, name='home'),
    path('toggle-lang/', toggle_lang, name='toggle_lang'),
    path('announce/', main_announce_view, name='announce'),
    path('events/', main_events_view, name='events'),
    path('useful-links/', main_useful_links_view, name='useful_links'),
    path('tuzuk/', main_tuzuk_view, name='tuzuk'),

    path('media/<path:path>', static_serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', static_serve, {'document_root': settings.STATIC_ROOT}),

    path('<path:name>/', flatpage_view, {'template': TEMPLATE, 'site': SITE})
]

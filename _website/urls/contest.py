from django.urls import path, include
from django.views.static import serve as static_serve

from django.conf import settings
from django.contrib import admin

from _website.views import *

SITE = 'contest'
TEMPLATE = 'contest_site/__flatpage.html'

handler404 = '_website.views.contest_error_view'
handler500 = '_website.views.contest_error_view'

urlpatterns = [
    path('1gan/', admin.site.urls),

    path('', contest_home_view, name= 'home'),
    path('toggle-lang/', toggle_lang, name='toggle_lang'),
    path('faq/', contest_faq_view, name='faq'),

    path('media/<path:path>', static_serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', static_serve, {'document_root': settings.STATIC_ROOT}),
    path('<path:name>/', flatpage_view, {'template': TEMPLATE, 'site': SITE})
]
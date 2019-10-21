from django.urls import path, include
from django.views.static import serve as static_serve

from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('1gan/', admin.site.urls),
    path('media/<path:path>', static_serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', static_serve, {'document_root': settings.STATIC_ROOT}),
    path('', include('_website.urls')),
]

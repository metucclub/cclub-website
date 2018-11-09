from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.views.static import serve

from filebrowser.sites import site as filebrowser_site

urlpatterns = [
    path('filebrowser/', filebrowser_site.urls),
    path('admin/', admin.site.urls),
    path('static/<str:path>/', serve, {'document_root': settings.STATIC_ROOT}),
    path('media/<str:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', include('main.urls')),
]


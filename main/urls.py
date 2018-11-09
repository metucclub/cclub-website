from django.urls import path, include
from django.contrib.flatpages import views as flatpage_views

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('announce/', views.announce_view, name='announce'),
    path('events/', views.events_view, name='events'),
    path('faydali-linkler/', views.useful_links_view, name='useful_links'),
    path('bergi/', views.bergi_view, name='bergi'),
    path('yarisma/', views.yarisma_view, name='yarisma'),
    path('tuzuk/', views.tuzuk_view, name='tuzuk'),

    path('about-us/', flatpage_views.flatpage, {'url': '/about-us/'}, name='about'),
    path('bilisimgunu/', flatpage_views.flatpage, {'url': '/bilisimgunu/'}, name='bilisim_gunu'),
    path('contact/', flatpage_views.flatpage, {'url': '/contact/'}, name='contact'),
]


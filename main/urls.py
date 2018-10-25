from django.conf.urls import url, include

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^about/$', views.about_view, name='about'),
    url(r'^announce/$', views.announce_view, name='announce'),
    url(r'^events/$', views.events_view, name='events'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^bilisimgunu/$', views.bilisim_gunu_view, name='bilisimgunu'),
    url(r'^bergi/$', views.bergi_view, name='bergi'),
    url(r'^yarisma/$', views.yarisma_view, name='yarisma'),
    url(r'^tuzuk/$', views.tuzuk_view, name='tuzuk'),
]


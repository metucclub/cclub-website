from django.conf.urls import url, include

from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home_view, name='home')
]


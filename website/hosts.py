from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host('yarisma', '_website.urls.contest', name='contest_site'),
    host('', '_website.urls.main', name='main_site'),
)
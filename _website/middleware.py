from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import Resolver404, resolve, reverse
from django.utils.http import urlquote

class HostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site = 1
        host = request.get_host()

        if host == 'yarisma.cclub2.metu.edu.tr':
            site = 2

        request.site = site

        request.trimmed_path = request.path

        if len(request.trimmed_path) > 1:
            if request.trimmed_path[0] == '/':
                request.trimmed_path = request.trimmed_path[1:]

            if request.trimmed_path[-1] == '/':
                request.trimmed_path = request.trimmed_path[:len(request.trimmed_path) - 1]

        return self.get_response(request)
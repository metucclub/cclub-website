from django.shortcuts import get_object_or_404
from django.utils import translation

from .models import Site

class LocaleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if translation.LANGUAGE_SESSION_KEY in request.session:
            lang = request.session[translation.LANGUAGE_SESSION_KEY]
        else:
            lang = translation.get_language()

        translation.activate(lang)
        request.LANGUAGE_CODE = lang

        return self.get_response(request)

class HostMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        site_id = 1
        host = request.get_host()

        site = Site.objects.filter(domain=host).first()

        if site:
            site_id = site.pk

        request.site = site_id

        request.trimmed_path = request.path

        if len(request.trimmed_path) > 1:
            if request.trimmed_path[0] == '/':
                request.trimmed_path = request.trimmed_path[1:]

            if request.trimmed_path[-1] == '/':
                request.trimmed_path = request.trimmed_path[:len(request.trimmed_path) - 1]

        return self.get_response(request)
from django.shortcuts import get_object_or_404

from .models import Site

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
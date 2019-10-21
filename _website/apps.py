from django.apps import AppConfig
from django.db import DatabaseError

class WebsiteConfig(AppConfig):
    name = '_website'

    def ready(self):
        from .models import Site

        try:
            Site.objects.all().exclude(pk__in=[1, 2]).delete()

            site = Site.objects.get_or_create(pk=1)[0]

            site.domain = 'cclub.metu.edu.tr'
            site.name = 'cclub'
            site.save()

            site = Site.objects.get_or_create(pk=2)[0]

            site.domain = 'yarisma.cclub.metu.edu.tr'
            site.name = 'yarisma'
            site.save()
        except DatabaseError:
            pass
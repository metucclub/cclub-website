from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.sites.models import Site

from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline, ]


admin.site.register(Event, EventAdmin)
admin.site.register(Announcement)
admin.site.register(UsefulLink)
admin.site.register(CarouselItem)

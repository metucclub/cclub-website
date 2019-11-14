from django.contrib import admin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.contrib.auth.models import User, Group

from .models import *

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline, ]

admin.site.register(Event, EventAdmin)

admin.site.register(Site)
admin.site.register(MenuItem)
admin.site.register(FlatPage)
admin.site.register(Announcement)
admin.site.register(UsefulLink)
admin.site.register(CarouselItem)
admin.site.register(ContestLanguage)
admin.site.register(ContestRule)
admin.site.register(FAQItem)

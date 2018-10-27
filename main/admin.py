# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Event, EventImage, Announcement, Option, UsefulLink

admin.site.unregister(User)
admin.site.unregister(Group)

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [ EventImageInline, ]

admin.site.register(Event, EventAdmin)
admin.site.register(Announcement)
admin.site.register(Option)
admin.site.register(UsefulLink)

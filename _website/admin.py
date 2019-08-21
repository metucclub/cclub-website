from django.contrib import admin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User, Group

from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)

csrf_protect_m = method_decorator(csrf_protect)

class SponsorImageInline(admin.TabularInline):
    model = SponsorImage
    extra = 0

# see https://github.com/praekelt/django-preferences/blob/develop/preferences/
class OptionsAdmin(admin.ModelAdmin):
    inlines = [SponsorImageInline, ]

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        """
        If we only have a single preference object redirect to it,
        otherwise display listing.
        """
        model = self.model
        if model.objects.all().count() > 1:
            return super(OptionsAdmin, self).changelist_view(request)
        else:
            obj = model.singleton.get()
            return redirect(
                reverse(
                    'admin:%s_%s_change' % (
                        model._meta.app_label, model._meta.model_name
                    ),
                    args=(obj.id,)
                )
            )

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline, ]

admin.site.register(Option, OptionsAdmin)
admin.site.register(Event, EventAdmin)

admin.site.register(FlatPage)
admin.site.register(Announcement)
admin.site.register(UsefulLink)
admin.site.register(CarouselItem)
admin.site.register(ContestSupportedLanguage)
admin.site.register(ContestRule)
admin.site.register(ContestFAQItem)
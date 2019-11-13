from django.db import models
from django.utils.timezone import now
from django.utils import translation

from martor.models import MartorField

from .utils import *

class Site(models.Model):
    display_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=20)

    custom_css = models.TextField(blank=True, null=True)
    custom_js = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    order = models.PositiveIntegerField(default=1)

    redirect_link = models.CharField(max_length=100, default='', blank=True)

    class Meta:
        ordering = ['site', 'order']

    def __str__(self):
        return '{} - {} - {}'.format(self.site.name, self.order, self.name)

class FlatPage(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    content_tr = MartorField()
    content_en = MartorField()

    blank_page = models.BooleanField(default=False)

    class Meta:
        ordering = ['site', 'name']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.name)

class CarouselItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)

    subtitle_tr = models.CharField(max_length=100, blank=True)
    subtitle_en = models.CharField(max_length=100, blank=True)

    image = models.ImageField()

    def __str__(self):
        return '{} - {} - {}'.format(self.site.name, self.title, self.pk)

class Event(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = MartorField()
    content_en = MartorField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

class Announcement(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = MartorField()
    content_en = MartorField()

    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)

class UsefulLink(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    title_tr = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)

    icon = models.CharField(max_length=20, blank=True, null=True, default='book')
    url = models.URLField()

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.title)

class ContestLanguage(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    name = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.name)

class ContestRule(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    content_tr = models.TextField()
    content_en = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.content)

class FAQItem(MultilingualModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    content_tr = models.TextField()
    content_en = models.TextField()

    answer_tr = models.TextField()
    answer_en = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.content)

class Sponsor(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    image = models.ImageField()

    def __str__(self):
        return '{} - {}'.format(self.site.name, self.pk)
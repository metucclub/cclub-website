# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.timezone import now
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    main_image = models.ImageField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images')
    image = models.ImageField()


class Announcement(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    time = models.DateTimeField(default=now)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']


class Option(models.Model):
    name = models.CharField(max_length=40)
    value = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return self.name


class UsefulLink(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=20, blank=True,
                            null=True, default='book')
    url = models.URLField()

    objects = models.Manager()

    def __str__(self):
        return self.title


class CarouselItem(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.title + ' - ' + self.subtitle

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField()

class Announcement(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    image = models.ImageField()
    time = models.DateTimeField(auto_now_add=True)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..lr_app.models import Users
# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

class Reviews(models.Model):
    review = models.TextField(null=True)
    user = models.ForeignKey(Users, related_name='reviews')
    book = models.ForeignKey(Books, related_name='reviews')
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0003_reviews_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='rating',
        ),
    ]
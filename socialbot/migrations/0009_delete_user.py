# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-16 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialbot', '0008_postmodel_has_liked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
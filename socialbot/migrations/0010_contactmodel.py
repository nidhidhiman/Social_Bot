# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-16 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialbot', '0009_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('subject', models.CharField(max_length=120)),
                ('feedback', models.CharField(max_length=2000)),
                ('number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=120)),
            ],
        ),
    ]

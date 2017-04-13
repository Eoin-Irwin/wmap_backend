# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-13 17:47
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DublinBikes',
            fields=[
                ('stand_number', models.IntegerField(primary_key=True, serialize=False, verbose_name='number')),
                ('stand_name', models.CharField(max_length=80, verbose_name='name')),
                ('total_bike_stands', models.IntegerField(verbose_name='bike_stands')),
                ('available_bike_stands', models.IntegerField(verbose_name='available_bike_stands')),
                ('available_bikes', models.IntegerField(verbose_name='available_bikes')),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('position', django.contrib.gis.db.models.fields.PointField(srid=6432, verbose_name='position')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('uid', models.CharField(blank=True, max_length=100, primary_key=True, serialize=False, verbose_name='uid')),
                ('uname', models.CharField(blank=True, max_length=80, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('last_location', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326, verbose_name='last_location')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

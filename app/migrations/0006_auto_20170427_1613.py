# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-27 15:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170419_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dublinbikes',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 27, 16, 13, 20, 594552)),
        ),
    ]

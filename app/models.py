import datetime

from django.utils import timezone

from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    uid = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='uid',
        primary_key=True
    )

    uname = models.CharField(
        verbose_name='name',
        max_length=80,
        blank=True,
    )

    email = models.EmailField(
        verbose_name='email')

    last_location = models.PointField(
        verbose_name="last_location",
        blank=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )


class DublinBikes(models.Model):
    stand_number = models.IntegerField(
        verbose_name='number',
        blank=False,
        primary_key=True
    )

    stand_name = models.CharField(
        max_length=80,
        verbose_name="name",
        blank=False
    )

    total_bike_stands = models.IntegerField(
        verbose_name="bike_stands",
        blank=False
    )

    available_bike_stands = models.IntegerField(
        verbose_name="available_bike_stands",
        blank=False
    )

    available_bikes = models.IntegerField(
        verbose_name="available_bikes",
        blank=False
    )

    last_update = models.DateTimeField(
        default=datetime.datetime.now()
    )

    position = models.PointField(
        verbose_name='position',
        srid=6432)

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

from django.db import models
from django.contrib.gis.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(models.Model):

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']

    user_id = models.IntegerField(
        verbose_name='user_id',
        blank=False,
        primary_key=True
    )

    name = models.CharField(
        verbose_name='name',
        max_length=80,
        blank=False,
    )

    email = models.EmailField(
        verbose_name='email',
        max_length=70,
        blank=True,
        unique=True)

    last_location = models.PointField(
        verbose_name="last known location",
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

    position = models.PointField(
        max_length=100,
        verbose_name="position",
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
        auto_now_add=True

    )
    user_id = models.ForeignKey(
        User,
        verbose_name='user_id',
        blank=False
    )


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.timestamp import TimeStampedModel
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser, TimeStampedModel):
    followings = models.ManyToManyField("self", related_name='followers', symmetrical=False)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = "사용자"
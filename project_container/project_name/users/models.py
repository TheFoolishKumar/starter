"""Defines Custom User Model for the project."""

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

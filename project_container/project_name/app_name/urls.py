"""URL Configuration for app_name goes here."""

from django.conf.urls import url
from .views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]

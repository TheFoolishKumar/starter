"""Main(Top-Level) URL Configuration goes here."""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Django Admin
    url(settings.ADMIN_URL, admin.site.urls),

    # flat pages

    # User management
    url(r'^users/', include('project_name.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Other Apps
    url(r'^', include('project_name.app_name.urls', namespace='app_name')),
]

if settings.DEBUG:
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns

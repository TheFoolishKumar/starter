"""Development Settings."""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django Debug Toolbar
INSTALLED_APPS += [
    'debug_toolbar',
    'project_name.app_name',
]

# Additional middleware introduced by debug toolbar
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Show emails to console in DEBUG mode
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Adding INETRNAL_IPS for Debug Toolbar
# See: https://django-debug-toolbar.readthedocs.io/en/stable/installation.html
INTERNAL_IPS = [
    '127.0.0.1',
]

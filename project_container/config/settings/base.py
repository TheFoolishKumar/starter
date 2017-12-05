"""Django settings for project."""

from os.path import dirname, join, exists
import environ

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
APPS_DIR = join(BASE_DIR, 'project_name')
STATICFILES_DIRS = [join(APPS_DIR, 'static')]
MEDIA_ROOT = join(APPS_DIR, 'media')
MEDIA_URL = "/media/"


# Use 12factor inspired environment variables or from a file
# import environ
env = environ.Env()

env_file = join(BASE_DIR, 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Google Signup using allauth
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(APPS_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Authentication Backends
# See: https://django-allauth.readthedocs.io/en/latest/installation.html

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^starter-admin/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# defaults for account creatio
# _______________________________________________________________________________

# ask for either username or email during login
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# Set Email field as required during signup
ACCOUNT_EMAIL_REQUIRED = True
# Set email versification necessary before creating account
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# Don't ask for username while signing up.
# Users can later edit/change username in their profile.
# If username is not set, use email to log in.
ACCOUNT_USERNAME_REQUIRED = False


# Log into account at '/accounts/login/'
LOGIN_URL = 'account_login'
# Redirect to '/app_name/home/' after successful login
LOGIN_REDIRECT_URL = '/app_name/home/'
# Redirect to '/app_name/home/' after logout
ACCOUNT_LOGOUT_REDIRECT_URL = '/app_name/home/'

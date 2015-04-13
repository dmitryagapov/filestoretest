from django.conf import settings
import os
import dj_database_url

# DATABASES = settings.DATABASES
DEBUG = False
TEMPLATE_DEBUG = True

PROJECT_DIRECTORY = os.getcwd()

# Parse database configuration from $DATABASE_URL


DATABASES = {
    'default': dj_database_url.config(),
}

BASE_DIR = settings.BASE_DIR


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


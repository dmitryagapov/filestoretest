from django.conf import settings
import os
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = True

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

STATICFILES_DIRS = (
    ('static', os.path.join(BASE_DIR, 'static')),
)


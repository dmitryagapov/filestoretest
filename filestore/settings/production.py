from django.conf import settings
import os

# DATABASES = settings.DATABASES
DEBUG = False
TEMPLATE_DEBUG = True

# Parse database configuration from $DATABASE_URL
import dj_database_url

# DATABASES['default'] =  dj_database_url.config()
BASE_DIR = settings.BASE_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_my.sqlite3'),
    }
}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
    # here you can add another templates directory if you wish.
)
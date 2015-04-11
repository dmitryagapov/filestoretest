from django.conf import settings
import os

DEBUG = False

TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES



# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    BASE_DIR + '/filestore/file/templates/',
    BASE_DIR + '/filestore/templates/',
    BASE_DIR + '/filestore/file/loginsys/templates/',

)
STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('static', 'C:/Users/Dmitry/DjangoProj/proj/filestore/static/'),
)

TEMPLATE_DIRS = settings.TEMPLATE_DIRS
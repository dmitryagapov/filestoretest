from django.conf import settings
import os

DEBUG = False

TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES



# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# TEMPLATE_DIRS = (
#     BASE_DIR + '/filestore/file/templates/',
#     BASE_DIR + '/filestore/templates/',
#     BASE_DIR + '/filestore/file/loginsys/templates/',
#
# )
STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('static', BASE_DIR + '/filestore/static/'),
)
# here() gives us file paths from the root of the system to the directory
# # holding the current file.
# here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
#
# PROJECT_ROOT = here("..")
# # root() gives us file paths from the root of the system to whatever
# # folder(s) we pass it starting at the parent directory of the current file.
# root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)
#
#
# TEMPLATE_DIRS = (
#     root('templates'),
# )


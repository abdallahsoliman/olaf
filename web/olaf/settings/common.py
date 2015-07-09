""" Common Settings and Globals """

from os.path import abspath, basename, dirname, join, normpath
from os import environ
from sys import path
from django.contrib.messages import constants as message_constants

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
DEBUG = False
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## DATABASE CONFIGURATION
# implement in the corresponding settings file (dev.py, prod.py, etc)
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
    'OOcontext_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',

    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'django.contrib.admin',
    'django.contrib.admindocs',
)
THIRD_PARTY_APPS = (
    # Static file management:
    'compressor',
    'rest_framework',
)
LOCAL_APPS = (
    'olaf',
    'authenticate',
)
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
LOGGING = {
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION


########## COMPRESSION CONFIGURATION
COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
########## END COMPRESSION CONFIGURATION

########## START TEST SETTINGS
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
########## END TEST SETTINGS

########## START AUTH SETTINGS
AUTH_USER_MODEL = 'authenticate.User'
########## END TEST SETTINGS

########## SECRET CONFIGURATION
SECRET_KEY = environ['SECRET_KEY']
########## END SECRET CONFIGURATION

########## DJANGO REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
########## END DJANGO REST FRAMEWORK CONFIGURATION

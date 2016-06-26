""" Development Settings and Globals """

from .common import *

########## DEBUG CONFIGURATION
DEBUG = True
########## END DEBUG CONFIGURATION

########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'olaf_dev',
        'USER': 'dev',
        'PASSWORD': 'dev@1994',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
########## END DATABASE CONFIGURATION

########## APP CONFIGURATION

THIRD_PARTY_APPS = (
    'django_extensions',
)
INSTALLED_APPS += THIRD_PARTY_APPS
########## END APP CONFIGURATION

########## START SESSION ENGINE CONFIGURATION
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
########## END SESSION ENGINE CONFIGURATION

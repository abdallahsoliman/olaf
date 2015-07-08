""" Development Settings and Globals """

from common import *

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
        'HOST': '192.168.1.4',
        'PORT': '5432',
    }
}
########## END DATABASE CONFIGURATION

########## APP CONFIGURATION

THIRD_PARTY_APPS = (
)
INSTALLED_APPS += THIRD_PARTY_APPS
########## END APP CONFIGURATION

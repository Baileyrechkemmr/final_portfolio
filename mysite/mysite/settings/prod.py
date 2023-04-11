import django_on_heroku 
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'baileyr-portfolio.herokuapp.com',
    'baileyr.portfolio',
]

DEBUG_propagate_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_exsiting_logggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple' : {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': { 
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# herocu settings 
django_on_heroku.settings(locals(), ststicfiles=False)
del DATABASES['default']['OPTIONS'] ['sslmode']
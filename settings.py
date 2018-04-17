#!/usr/bin/env python3

from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/database.sqlite3',
    }
}

DEBUG=True
APPEND_SLASH=True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


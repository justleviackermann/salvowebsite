from .settings import *
import os
from pathlib import Path
#i created this file for migrating sqlite to postgres and i hope it might be useful someday so pushing it
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'tracker': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME' : BASE_DIR / 'db-tracker.sqlite3',
    }
}

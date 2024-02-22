import os
from gef_mysql_config import db_host, db_user, db_password, db_name

from .settings import *

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "generate_new_valid_key")

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

del STATICFILES_DIRS
STATIC_ROOT = BASE_DIR / "static"

from .common import *
from decouple import config
DEBUG = True

ALLOWED_HOSTS = ['.localhost','127.0.0.1']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD")
    }
}
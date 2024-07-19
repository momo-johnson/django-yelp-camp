import os
from django.contrib.messages import constants as messages
from django.urls import reverse_lazy
from decouple import config, Csv
import cloudinary


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.sites',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'comments',
    'campgrounds',
    'widget_tweaks',
    'avatar',
]

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoyelpcamp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGIN_URL = 'auth_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Django registration redux settings
SITE_ID = 1
ACCOUNT_ACTIVATION_DAYS = 3
DEFAULT_FROM_EMAIL = 'Django Yelp Camp Team <noreply@djangoyelcamp.site>'
EMAIL_SUBJECT_PREFIX = '[Django Yelp Camp]'
REGISTRATION_EMAIL_HTML = True
REGISTRATION_AUTO_LOGIN = True

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # config('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_BACKEND = 'accounts.backends.email_backend.EmailBackend' 
EMAIL_HOST = config('EMAIL_HOST', cast=str)
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)



os.environ["GOOGLE_API_KEY"] = config('GOOGLE_API_KEY', cast=str)
# STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DEFAULT_AUTO_FIELD='django.db.models.AutoField' 

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

cloudinary.config(
    cloud_name = config('CLOUDINARY_CLOUD_NAME', cast=str),
    api_key = config('CLOUDINARY_API_KEY', cast=str),
    api_secret = config('COUDINARY_API_SECRET', cast=str)
)

STORAGES = {
   "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
    
}


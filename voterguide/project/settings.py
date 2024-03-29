"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '55bg!26p+399rnh$-8++h6l%l+2o1(381^p)2ejgm^pck5zi!='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.bettergov.org',
    '.elasticbeanstalk.com',
    '127.0.0.1',
    'localhost'
]


# Application definition

INSTALLED_APPS = [
    'ckeditor',
    'storages',
    'qas.apps.QasConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'votersguide',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '',
            'PORT': ''
        }
    }




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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(BASE_DIR, "www/static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "www/static")
]

MEDIA_ROOT = os.path.join(BASE_DIR, "www/media")
MEDIA_URL = '/media/'

# CKEditor configuration
# https://docs.ckeditor.com/ckeditor4/latest/guide/dev_configuration.html

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['Format', 'RemoveFormat', 'Source'],
            ['Image']
        ],
        'height': 150,
        'extraAllowedContent': 'div(class),a(href,class)',
    }
}

# AWS S3 settings
PROJECT_NAME = 'voter-guide'
AWS_STORAGE_BUCKET_NAME = 'media.bettergov.org'
AWS_S3_REGION_NAME = 'us-east-1'  # e.g. us-east-2
# AWS_ACCESS_KEY_ID = 'xxxxxxxxxxxxxxxxxxxx'
# AWS_SECRET_ACCESS_KEY = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'

# Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME

# Tell the staticfiles app to use S3Boto3 storage when writing the collected
# static files (when you run `collectstatic`).
STATICFILES_LOCATION = os.path.join(PROJECT_NAME, 'static')
if 'RDS_DB_NAME' in os.environ:
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = os.path.join(PROJECT_NAME, 'media')
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# django bakery
BUILD_DIR = os.path.join(os.path.dirname(BASE_DIR), 'build')
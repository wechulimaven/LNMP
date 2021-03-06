"""
Django settings for mpesa project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# from decouple import config
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k0x3bsr8+%o-)n&8ooz(7w7a45$wgnjjhu11er$!3$@pabg***'
# config('SECREAT_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    # 'rest_auth',
    'daraja',
    'mpesacallbackAPI',
    'ussd'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mpesa.urls'

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

WSGI_APPLICATION = 'mpesa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES['default'].update(db_from_env)




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# BUSNESS_SHORT_CODE=config('BUSNESS_SHORT_CODE')
# TRANSACTION_TYPE = config('TRANSACTION_TYPE')
# TRANSACTION_DESCRIPTION= config('TRANSACTION_DESCRIPTION')
# ACCOUNT_REFERENCE = config('ACCOUNT_REFERENCE')
# API_RESOURCE_URL = config('API_RESOURCE_URL')
# ACCESS_TOKEN_URL = config('ACCESS_TOKEN_URL')
# LIPANAMPESA_PASSKEY = config('LIPANAMPESA_PASSKEY')
# CONSUMER_KEY = config('CONSUMER_KEY')
# CONSUMER_SECRETE = config('CONSUMER_KEY')
BUSNESS_SHORT_CODE='174379'
TRANSACTION_TYPE = 'CustomerPayBillOnline'
TRANSACTION_DESCRIPTION= 'Payment of X'
ACCOUNT_REFERENCE = 'CompanyXLTD'
API_RESOURCE_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
# API_RESOURCE_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query'
# ACCESS_TOKEN_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
ACCESS_TOKEN_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
LIPANAMPESA_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
CONSUMER_KEY = 'DykAs3IoKpAsDIkSSnG5YuG43oGF2JEi'
CONSUMER_SECRETE = 'bvF74G0aXKZqGcTj'


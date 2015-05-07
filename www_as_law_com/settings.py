"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uzyz3y(3(+uq5!!_2(rt8@p#p99$3)h-c8i$cp1ap9q58n5$rm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['www.as-law.be','as-law.be']

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'as_law'
EMAIL_HOST_PASSWORD = 'Abcd1234'
DEFAULT_FROM_EMAIL = 'avocats@as-law.be'
SERVER_EMAIL = 'avocats@as-law.be'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'signups',    	
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'www_as_law_com.urls'

WSGI_APPLICATION = 'www_as_law_com.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'www_as_law_com_db',
        'USER':'netsamir',
        'PASSWORD':'Abcd1234',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


if not DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/home/netsamir/webapps/as_law_static/'
    MEDIA_ROOT =  '/home/netsamir/webapps/as_law_static/media'
    STATICFILES_DIRS = (
	'/home/netsamir/webapps/as_law_static/static',
    )

# netsamir: Template location
    TEMPLATE_DIRS = (
    	'/home/netsamir/webapps/as_law_static/templates',
    )

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'www_as_law_com.settings'

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()

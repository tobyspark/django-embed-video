import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

if django.VERSION[:2] >= (1, 7):
    django.setup()

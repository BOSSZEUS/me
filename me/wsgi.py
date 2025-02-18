"""
WSGI config for me project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
# filepath: /C:/Users/jorda/OneDrive/Desktop/code/Django/me/me/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'me.settings')

application = get_wsgi_application()

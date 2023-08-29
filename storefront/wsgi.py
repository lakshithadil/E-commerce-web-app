"""
WSGI config for storefront project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = (
    "storefront.settings.prod"
    if "WEBSITE_HOSTNAME" in os.environ
    else "storefront.settings.dev"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()

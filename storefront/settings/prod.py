import os
from .common import *

DEBUG = True

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)
CSRF_TRUSTED_ORIGINS = (
    ["https://" + os.environ["WEBSITE_HOSTNAME"]]
    if "WEBSITE_HOSTNAME" in os.environ
    else []
)

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["AZURE_MYSQL_NAME"],
        "HOST": os.environ["AZURE_MYSQL_HOST"],
        "USER": os.environ["AZURE_MYSQL_USER"],
        "PASSWORD": os.environ["AZURE_MYSQL_PASSWORD"],
    }
}

# conn_str = os.environ["AZURE_POSTGRESQL_CONNECTIONSTRING"]
# conn_str_params = {
#     pair.split("=")[0]: pair.split("=")[1] for pair in conn_str.split(" ")
# }
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": conn_str_params["dbname"],
#         "HOST": conn_str_params["host"],
#         "USER": conn_str_params["user"],
#         "PASSWORD": conn_str_params["password"],
#     }
# }

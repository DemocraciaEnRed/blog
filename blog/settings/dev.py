from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7@ce-yhd$yhjar_7=sl+i26l0xaa=vi^j!@23vn2ez2dud1%41"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://*.democraciaenred.org']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Default storage settings, with the staticfiles storage updated.
# See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # ManifestStaticFilesStorage is recommended in production, to prevent
    # outdated JavaScript / CSS assets being served from cache
    # (e.g. after a Wagtail upgrade).
    # See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}



try:
    from .local import *
except ImportError:
    pass

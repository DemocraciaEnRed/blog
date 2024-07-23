from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://*.democraciaenred.org']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Configuración de almacenamiento estático y de medios
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Configuración de AWS S3 para DigitalOcean Spaces
AWS_S3_FILE_OVERWRITE = False
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL')
AWS_LOCATION = os.environ.get('AWS_LOCATION')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


try:
    from .local import *
except ImportError:
    pass

from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Nm_2Vw-Se8HAbhlKLR2GKnkYopZqOkgi9Qw4PXn29AtDJHgKJKc"
    ,)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

LOGGING = {
    "version" : 1,
    "disable_existing_loggers": False,
    "formatters" : {
        "verbose" : {
            "format" : "%(levelname)s %(name)-12s %(asctime)s %(module)s"
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers" : {
        "console" : {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter" : "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers" : ["console"]
    },
}
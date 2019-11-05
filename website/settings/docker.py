from .base import *

DEBUG = False

DATABASES = {
    "default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": os.environ.get("db_name"),
		"USER": os.environ.get("db_user"),
		"HOST": os.environ.get("db_host"),
		"PASSWORD": os.environ.get("db_pass"),
    }
}

ALLOWED_HOSTS = ['*']

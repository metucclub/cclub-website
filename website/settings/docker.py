from .base import *

PARENT_HOST = 'cclub.metu.edu.tr'

DEBUG = False

DATABASES = {
    "default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": os.environ.get("db_name"),
		"USER": os.environ.get("db_user"),
		"HOST": os.environ.get("db_host"),
    }
}

ALLOWED_HOSTS = ['yarisma.cclub.metu.edu.tr', 'cclub.metu.edu.tr', 'www.cclub.metu.edu.tr']

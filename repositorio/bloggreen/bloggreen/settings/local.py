from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
#    "default": {
#        "ENGINE": "sql_server.pyodbc",
#        "NAME": "bloggreen",
#        "Trusted_Connection" : "yes",
#        "HOST": "localhost",
#        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
#        },
#    },

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


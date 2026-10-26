from mysite.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!%cuu$re(=521rwl8fa3hri+of(76s!_e6=ii-$zfs2!o3_6&*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'testserver']

#sitemaps
SITE_ID = 1

#INSTALLED_APS: []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [ #other static directory that consider as valid static dir 
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS = 'DENY'

from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CarlosLazovich$default',
        'USER': 'CarlosLazovich',
        'PASSWORD': 'josema39938597',
        'HOST': 'CarlosLazovich.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}

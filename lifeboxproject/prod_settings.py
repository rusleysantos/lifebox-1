from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lifebox$default',
        'USER': 'lifebox',
        'PASSWORD': 'vermelho@123',
        'HOST': 'lifebox.mysql.pythonanywhere-services.com',
    }
}
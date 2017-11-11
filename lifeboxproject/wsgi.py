"""
Configuração WSGI para a função de uploads (carregar arquivos).
Ele expõe o WSGI chamado como uma variável de nível de módulo chamada `` application``.
Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifeboxproject.settings")
# Heroku
application = get_wsgi_application()
# application = DjangoWhiteNoise(application)

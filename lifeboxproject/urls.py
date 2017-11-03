from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('monitoramento.urls')),
    url(r'^monitoramento/', include('monitoramento.urls')),
    url(r'^relatorios/', include('relatorios.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^cadastro/', include('core.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^io/', include('django_socketio.urls')),
]
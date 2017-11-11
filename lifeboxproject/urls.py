from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('monitoramento.urls')),
    #url(r'^monitoramento/', include('monitoramento.urls')),
    url(r'^relatorios/', include('relatorios.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^cadastro/', include('core.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^import/csv/$', views.importa_arquivo, name='importa_arquivo'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

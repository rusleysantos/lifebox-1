# -*- coding: utf-8 -*-
from django.conf.urls import url
from monitoramento import views

urlpatterns = [
    url(r'^$', views.mapas, name='exibir_mapa'),
    url(r'^(?P<pk>\d+)/$', views.mapaplayback, name='exibir_mapa_playback'),
]

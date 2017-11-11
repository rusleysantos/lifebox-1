# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from core import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^caixa/$', views.caixa_pesquisar, name='caixa_pesquisar'),
    url(r'^caixa/add$', views.caixa_criar, name='caixa_criar'),
    url(r'^caixa/(?P<pk>\d+)/$', views.caixa_editar, name='caixa_editar'),
    url(r'^caixa/exp/$', views.caixa_exportar, name='caixa_exportar'),
    url(r'^caixa/imp/$', views.caixa_importar, name='caixa_importar'),

    url(r'^equipamento/$', views.equipamento_pesquisar, name='equipamento_pesquisar'),
    url(r'^equipamento/add$', views.equipamento_criar, name='equipamento_criar'),
    url(r'^equipamento/(?P<pk>\d+)/$', views.equipamento_editar, name='equipamento_editar'),
    url(r'^equipamento/exp/$', views.equipamento_exportar, name='equipamento_exportar'),
    url(r'^equipamento/imp/$', views.equipamento_importar, name='equipamento_importar'),

    url(r'^hospital/$', views.hospital_pesquisar, name='hospital_pesquisar'),
    url(r'^hospital/add$', views.hospital_criar, name='hospital_criar'),
    url(r'^hospital/(?P<pk>\d+)/$', views.hospital_editar, name='hospital_editar'),
    url(r'^hospital/exp/$', views.hospital_exportar, name='hospital_exportar'),
    url(r'^hospital/imp/$', views.hospital_importar, name='hospital_importar'),

    url(r'^viagem/$', views.viagem_pesquisar, name='viagem_pesquisar'),
    url(r'^viagem/add$', views.viagem_criar, name='viagem_criar'),
    url(r'^viagem/(?P<pk>\d+)/$', views.viagem_editar, name='viagem_editar'),
    url(r'^viagem/exp/$', views.viagem_exportar, name='viagem_exportar'),
    url(r'^viagem/imp/$', views.viagem_importar, name='viagem_importar'),

    url(r'^importa/$', views.importa, name='importa'),
    url(r'^importa/exp/$', views.importa_arquivo, name='importa_arquivo'),

    url(r'^viagem/(?P<pk>\d+)/status/(?P<cod>\d+)/', views.status_alterar, name='status_editar'),



    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    #url(r'^viagem/(?P<pk>\d+)/upload/', views.upload_file, name='upload_file'),
]

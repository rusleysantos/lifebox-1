# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^equipamento/$', views.equipamento_pesquisar, name='equipamento_pesquisar'),
    url(r'^equipamento/add$', views.equipamento_criar, name='equipamento_criar'),
    url(r'^equipamento/(?P<pk>\d+)/$', views.equipamento_editar, name='equipamento_editar'),
    url(r'^caixa/$', views.caixa_pesquisar, name='caixa_pesquisar'),
    url(r'^caixa/add$', views.caixa_criar, name='caixa_criar'),
    url(r'^caixa/(?P<pk>\d+)/$', views.caixa_editar, name='caixa_editar'),
    url(r'^hospital/$', views.hospital_pesquisar, name='hospital_pesquisar'),
    url(r'^hospital/add$', views.hospital_criar, name='hospital_criar'),
    url(r'^hospital/(?P<pk>\d+)/$', views.hospital_editar, name='hospital_editar'),
    url(r'^viagem/$', views.viagem_pesquisar, name='viagem_pesquisar'),
    url(r'^viagem/add$', views.viagem_criar, name='viagem_criar'),
    url(r'^viagem/(?P<pk>\d+)/$', views.viagem_editar, name='viagem_editar'),
    url(r'^viagem/(?P<pk>\d+)/status/(?P<cod>\d+)/', views.status_alterar, name='status_editar'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^equipe/$', views.equipe, name='equipe'),
    #url(r'^viagem/(?P<pk>\d+)/upload/', views.upload_file, name='upload_file'),
]

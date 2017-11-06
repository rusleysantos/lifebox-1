# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from rest_framework import routers
from api import apis


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'viagem', apis.ViagemViewSet)
router.register(r'viagem-ativas', apis.ViagemAtivasViewSet)
router.register(r'detalhe', apis.DetalheViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

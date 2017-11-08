# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework import generics
from core.models import Viagem, Detalhe
from .serializers import UserSerializer, ViagemSerializer, DetalheSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

class ViagemAtivasViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.filter(status = 3)
    serializer_class = ViagemSerializer

class DetalheViewSet(viewsets.ModelViewSet):
    queryset = Detalhe.objects.all()
    serializer_class = DetalheSerializer
    
class DetalheListViewSet(generics.ListCreateAPIView):
    queryset = Detalhe.objects.all()
    serializer_class = DetalheSerializer

class DetalheDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalhe.objects.all()
    serializer_class = DetalheSerializer

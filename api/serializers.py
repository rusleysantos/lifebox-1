# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Detalhe, Viagem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DetalheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalhe
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):
    detalhes = DetalheSerializer(many=True, read_only=True)
    
    class Meta:
        model = Viagem
        fields = '__all__'
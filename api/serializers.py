# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Detalhe, Viagem, Hospital, Equipamento, Caixa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CaixaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caixa
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class DetalheSerializer(serializers.ModelSerializer):
    #imeiEquipamento = serializers.CharField(max_length=22)
    
    class Meta:
        model = Detalhe
        fields = '__all__'

class ViagemSerializer(serializers.ModelSerializer):
    detalhes = DetalheSerializer(many=True, read_only=True)
    caixa = CaixaSerializer(read_only=True)
    localPartida = HospitalSerializer(read_only=True)
    localChegada = HospitalSerializer(read_only=True)
    
    class Meta:
        model = Viagem
        fields = '__all__'
        
class ViagemSimpleSerializer(serializers.ModelSerializer):
    caixa = CaixaSerializer(read_only=True)
    
    class Meta:
        model = Viagem
        fields = '__all__'
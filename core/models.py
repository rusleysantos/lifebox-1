# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

###################################################################################################
# Banco Equipamento:
OPERADORA_CHOICES = (
    ('Vivo', 'Vivo'),
    ('Oi', 'Oi'),
    ('Tim', 'Tim'),
    ('Claro', 'Claro'),
    ('Nextel', 'Nextel'),
)

class Equipamento(models.Model):
    nome = models.CharField('Equipamento', max_length=5)
    imeiEquipamento = models.CharField('IMEI do Equipamento', max_length=22)
    telefone = models.CharField('Telefone', max_length=22)
    operadora = models.CharField('Operadora', max_length=8, choices=OPERADORA_CHOICES)
    imeiSimCard = models.CharField('IMEI SIM Card', max_length=26)


    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

###################################################################################################
# Banco Caixa:
class Caixa(models.Model):
    idCaixa= models.CharField('Identificação da Caixa', max_length=5)
    autorizacao= models.CharField('Autorização da Caixa', max_length=50)
    corCaixa= models.CharField('Cor da Tarja', max_length=7, null=True)
    informacaoAdicional= models.TextField('Informações Adicionais', max_length=100)


    def publish(self):
        self.save()

    def __str__(self):
        return self.idCaixa

###################################################################################################
# Banco Hospital:
class Hospital(models.Model):
    nome = models.CharField('Nome do Hospital', max_length=50)
    telefone = models.CharField('Telefone', max_length=19)
    nomeResponsavel = models.CharField('Responsável', max_length=30)
    emailResponsavel = models.CharField('E-mail', max_length=50)
    cep = models.CharField('CEP',max_length=10)
    logradouro = models.CharField('Endereço',max_length=50)
    bairro = models.CharField('Bairro',max_length=30)
    cidade = models.CharField('Cidade',max_length=30)
    uf = models.CharField('UF',max_length=2)


    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return u'{f}'.format(f=self.nome)

    class Meta:
        verbose_name_plural = 'Hospitais'

# Banco Status:
class Status(models.Model):
    codStatus = models.CharField(max_length=2)
    dscStatus = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)
        
    def __unicode__(self):
        return u'{f}'.format(f=self.dscStatus)
    
    class Meta:
        verbose_name_plural = 'Status'
        verbose_name = 'Status'


###################################################################################################
# Banco Viagem:
class Viagem(models.Model):
    localPartida = models.ForeignKey('Hospital', related_name='local_partida')
    localChegada = models.ForeignKey('Hospital', related_name='local_chegada')
    caixa = models.ForeignKey('Caixa')
    equipamento = models.ForeignKey('Equipamento')
    status = models.ForeignKey('Status', related_name='status', default=1)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Viagens'
        verbose_name = 'Viagem'

class Detalhe(models.Model):
    numLongitudeDeta = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    numLatitudeDeta = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    numTemperaturaDeta = models.IntegerField('Temperatura')
    indVirouDeta = models.BooleanField('Virou?', )
    indTombouDeta = models.BooleanField('Tombou?', )
    viagem = models.ForeignKey('Viagem', related_name='detalhes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
      verbose_name = u"Detalhe"
      verbose_name_plural = u"Detalhes"
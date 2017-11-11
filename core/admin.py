# -*- coding: utf-8 -*-
# importaçoes originais do admin.py -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from core.models import Equipamento, Caixa, Hospital, Viagem, Status, Detalhe, Importa

# importaçoes para atender função importa/exporta
from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from import_export import resources


################################################################################
#Habilita importar e exportar no ADMIM - Modulo Equipamento
class EquipamentoResource(resources.ModelResource):
    class Meta:
        model = Equipamento
        fields = ('id','idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard','createdEm','createdPor')

class EquipamentoAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EquipamentoResource
    def get_resource_class(self):
        if not self.resource_class:
            return EquipamentoResource
        else:
            return self.resource_class


admin.site.register(Equipamento, EquipamentoAdmin)

################################################################################
#Habilita importar e exportar no ADMIM - Modulo CAIXA
class CaixaResource(resources.ModelResource):
    class Meta:
        model = Caixa
        fields  =  ( 'id', 'idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional','createdEm','createdPor')

class CaixaAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CaixaResource
    def get_resource_class(self):
        if not self.resource_class:
            return CaixaResource
        else:
            return self.resource_class

admin.site.register(Caixa, CaixaAdmin)

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Hospital
class HospitalResource(resources.ModelResource):
    class Meta:
        model = Hospital
        fields = ('id', 'nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf','createdEm','createdPor')

class HospitalAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = HospitalResource
    def get_resource_class(self):
        if not self.resource_class:
            return HospitalResource
        else:
            return self.resource_class

admin.site.register(Hospital, HospitalAdmin)

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Viagem
class ViagemResource(resources.ModelResource):
    class Meta:
        model = Viagem
        fields = ('id', 'localPartida', 'localChegada', 'caixa', 'equipamento', 'status', 'nomeTransportador', 'contato', 'obs','createdEm','createdPor')

class ViagemAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ViagemResource
    def get_resource_class(self):
        if not self.resource_class:
            return ViagemResource
        else:
            return self.resource_class
admin.site.register(Viagem, ViagemAdmin)

class DetalheAdmin(admin.ModelAdmin):
    list_display = ('id','numLongitudeDeta', 'numLatitudeDeta', 'numTemperaturaDeta')
    
admin.site.register(Detalhe, DetalheAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','codStatus', 'dscStatus')
    
admin.site.register(Status, StatusAdmin)

admin.site.register(Importa)
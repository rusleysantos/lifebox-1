from import_export import resources
from core.models import Equipamento, Caixa, Hospital, Viagem, Status, Detalhe, Importa

"""
################################################################################
#Habilita importar e exportar no ADMIM - Modulo Equipamento
class EquipamentoResource(resources.ModelResource):
    class Meta:
        model = Equipamento
        fields = ('id', 'idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard','createdEm','createdPor')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo CAIXA
class CaixaResource(resources.ModelResource):
    class Meta:
        model = Caixa
        fields  =  ( 'idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional','createdEm','createdPor')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Hospital
class HospitalResource(resources.ModelResource):
    class Meta:
        model = Hospital
        fields = ('nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf','createdEm','createdPor')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Viagem
class ViagemResource(resources.ModelResource):
    class Meta:
        model = Viagem
        fields = ('localPartida', 'localChegada', 'caixa', 'equipamento', 'status', 'nomeTransportador', 'contato', 'obs','createdEm','createdPor')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Status
class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        fields  =  ( 'codStatus', 'dscStatus')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Detalhe
class DetalheResource(resources.ModelResource):
    class Meta:
        model = Detalhe
        fields  =  ( 'numLongitudeDeta','numLatitudeDeta','numTemperaturaDeta','indVirouDeta','indTombouDeta','viagem','createdEm','createdPor')

################################################################################
#Habilita importar e exportar no ADMIM - Modulo Importa
class ImportaResource(resources.ModelResource):
    class Meta:
        model = Importa
        fields  =  ('imei','dia','hora','longitude','latitude','altitude','velocidade','temperatura','vibra','tombo','course','satelites','createdEm','createdPor')

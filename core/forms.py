# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput, Textarea, DateTimeInput
from .models import Equipamento, Caixa, Hospital, Viagem
from django.contrib.auth.models import User # carrega user para inserção no campo createdPor

###################################################################################################
# Formulário Equipamento:
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard', 'createdEm', 'createdPor')
        widgets = {
            'id': TextInput(attrs={'readonly': 'True'}),
            'idEquipamento': TextInput(attrs={'class':'eq_mask'}),
            'imeiEquipamento': TextInput(attrs={'class': 'imeiTracker'}),
            'telefone': TextInput(attrs={'class': 'phone'}),
            'imeiSimCard': TextInput(attrs={'class': 'imeiSimCard'}),
            'createdEm' : DateTimeInput(attrs={'readonly': 'True'}),
            }


class DataInput(forms.Form):
    file = forms.FileField()


def save(self):
    records = csv.reader(self.cleaned_data["file"])
    for line in records:
        parts = Caixa()
        parts.supplier_id = line[0]
        parts.name = line[1]
        parts.description = line[2]
        parts.save()

###################################################################################################
# Formulário Caixa:
class CaixaForm(forms.ModelForm):
   class Meta:
       model = Caixa
       fields = ('idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional', 'createdEm', 'createdPor')
       widgets = {
                'id': TextInput(attrs={'readonly': 'True'}),
                'idCaixa': TextInput(attrs={'class':'cx_mask'}),
                'corCaixa': TextInput(attrs={'type': 'color'}),
                'informacaoAdicional': Textarea(attrs={'rows':'5', 'onkeyup':"mostrarResultado(this.value,200,'spcontando');contarCaracteres(this.value,200,'sprestante')"}),
                'createdEm' : DateTimeInput(attrs={'readonly': 'True'}),
                }

###################################################################################################
# Formulário Hospital:
class HospitalForm(forms.ModelForm):
   class Meta:
       model = Hospital
       fields = ('nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf', 'createdEm', 'createdPor')
       widgets = {
           'id': TextInput(attrs={'readonly': 'True'}),
           'telefone': TextInput(attrs={'class': 'phone'}),
           'cep': TextInput(attrs={'class': 'cep'}),
           'logradouro': TextInput(attrs={'autocomplete': 'on'}),
           'bairro': TextInput(attrs={'autocomplete': 'on'}),
           'cidade': TextInput(attrs={'autocomplete': 'on'}),
           'uf': TextInput(attrs={'autocomplete': 'on'}),
           'createdEm' : DateTimeInput(attrs={'readonly': 'True'}),
           }


###################################################################################################
# Formulário Viagem:
class ViagemForm(forms.ModelForm):
   class Meta:
       model = Viagem
       fields = ('localPartida', 'localChegada', 'caixa', 'equipamento', 'nomeTransportador', 'contato', 'obs', 'createdEm', 'createdPor')
       widgets = {
           'id': TextInput(attrs={'readonly': 'True'}),
           'contato': TextInput(attrs={'class': 'phone'}),
           'obs': Textarea(attrs={'rows':'5', 'onkeyup':"mostrarResultado(this.value,500,'spcontando');contarCaracteres(this.value,500,'sprestante')"}),
           'createdEm' : DateTimeInput(attrs={'readonly': 'True'}),
           }


class UploadFileForm(forms.Form):
    file = forms.FileField(label = '' , widget = forms.FileInput(attrs={'accept':"*.*", 'class':'custom-file-input'}))
# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput
from .models import Equipamento, Caixa, Hospital, Viagem


###################################################################################################
# Formulário Equipamento:
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ('nome', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard')
        widgets = {
            'nome': TextInput(attrs={'readonly': 'True'}),
            'imeiEquipamento': TextInput(attrs={'class': 'imeiTracker'}),
            'telefone': TextInput(attrs={'class': 'phone'}),
            'imeiSimCard': TextInput(attrs={'class': 'imeiSimCard'}),
            }


###################################################################################################
# Formulário Caixa:
class CaixaForm(forms.ModelForm):
   class Meta:
       model = Caixa
       fields = ('idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional')
       widgets = {
           'idCaixa': TextInput(attrs={'readonly': 'True'}),
           'corCaixa': TextInput(attrs={'type': 'color'}),
       }

###################################################################################################
# Formulário Hospital:
class HospitalForm(forms.ModelForm):
   class Meta:
       model = Hospital
       fields = ('nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf')
       widgets = {
           'id': TextInput(attrs={'readonly': 'True'}),
           'telefone': TextInput(attrs={'class': 'phone'}),
           'cep': TextInput(attrs={'class': 'cep'}),
           'logradouro': TextInput(attrs={'autocomplete': 'on'}),
           'bairro': TextInput(attrs={'autocomplete': 'on'}),
           'cidade': TextInput(attrs={'autocomplete': 'on'}),
           'uf': TextInput(attrs={'autocomplete': 'on'}),
           }


###################################################################################################
# Formulário Viagem:
class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ('localPartida', 'localChegada', 'caixa', 'equipamento')


class UploadFileForm(forms.Form):
    file = forms.FileField(label = '' , widget = forms.FileInput(attrs={'accept':"*.*", 'class':'custom-file-input'}))
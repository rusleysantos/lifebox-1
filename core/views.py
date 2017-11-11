# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage # acho que não se usa mais ..a pagnação agora é na tabela
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect

from core.models import Equipamento, Caixa, Hospital, Viagem, Status
from core.forms import EquipamentoForm, CaixaForm, HospitalForm, ViagemForm, UploadFileForm
from core.forms import EquipamentoForm, CaixaForm, HospitalForm, ViagemForm
from tablib import Dataset # Importante para a função de importar/exportar arquivos no admin django
from import_export.admin import ExportMixin # Importante para a função de importar/exportar arquivos sem admin django
from django.http import JsonResponse, HttpResponse #HttpResponse é para testes com export e import
from .models import Equipamento, Caixa, Hospital, Viagem, Status
from django.core.files.storage import FileSystemStorage
import csv


###################################################################################################
# Cadastro de Equipamentos:
@login_required
def equipamento_pesquisar(request): # Filtra os equipamentos:
        equipamentos = Equipamento.objects.all()
        return render(request, 'equipamento/pesquisa.html', {'equipamentos': equipamentos})

def equipamento_criar(request):
        if request.method == 'POST':
            form = EquipamentoForm(request.POST)
            if form.is_valid():
                equipamento = form.save(commit=False)
                equipamento.save()
            return redirect('equipamento_pesquisar')
        else:
            form = EquipamentoForm()
        return render(request, 'equipamento/formulario.html', {'form': form})


def equipamento_editar(request, pk):
        equipamento = get_object_or_404(Equipamento, pk=pk)
        if request.method == "POST":
            form = EquipamentoForm(request.POST, instance=equipamento)
            if form.is_valid():
                equipamento = form.save(commit=False)
                equipamento.save()
            return redirect('equipamento_pesquisar')
        else:
            form = EquipamentoForm(instance=equipamento)
        return render(request, 'equipamento/formulario.html', {'form': form})


def equipamento_exportar(request):
        response = HttpResponse (content_type='text/csv')
        response ['Content-Disposition'] = 'attachment; filename = "Equipamentos.csv"'
        writer = csv.writer(response)
        writer.writerow ([ 'id', 'idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard', 'createdEm', 'createdPor'])
        equipamentos = Equipamento.objects.all().values_list( 'id', 'idEquipamento', 'imeiEquipamento', 'telefone', 'operadora', 'imeiSimCard', 'createdEm', 'createdPor')
        for equipamento in equipamentos:
            writer.writerow(equipamento)
        return response

def equipamento_importar(request):
        equipamentos = Equipamento.objects.all()
        return render(request, 'equipamento/pesquisa.html', {'equipamentos': equipamentos})


###################################################################################################
# Cadastro de Caixas:
@login_required
def caixa_pesquisar(request):
        caixas = Caixa.objects.all()
        return render(request, 'caixa/pesquisa.html', {'caixas': caixas})


def caixa_criar(request):
        if request.method == 'POST':
            form = CaixaForm(request.POST)
            if form.is_valid():
                caixa = form.save(commit=False)
                caixa.save()
            return redirect('caixa_pesquisar')
        else:
            form = CaixaForm()
            return render(request, 'caixa/formulario.html', {'form': form})


def caixa_editar(request, pk):
        caixa = get_object_or_404(Caixa, pk=pk)
        if request.method == "POST":
            form = CaixaForm(request.POST, instance=caixa)
            if form.is_valid():
                caixa = form.save(commit=False)
                caixa.save()
            return redirect('caixa_pesquisar')
        else:
            form = CaixaForm(instance=caixa)
        return render(request, 'caixa/formulario.html', {'form': form})

def caixa_exportar(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Caixas.csv"'
    writer = csv.writer(response)
    writer.writerow(['id', 'idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional', 'createdEm', 'createdPor'])
    caixas = Caixa.objects.all().values_list( 'id', 'idCaixa', 'autorizacao', 'corCaixa', 'informacaoAdicional', 'createdEm', 'createdPor')
    for caixa in caixas:
        writer.writerow(caixa)
    return response



def caixa_importar(request):
    caixas = Caixa.objects.all()
    return render(request, 'caixa/pesquisa.html', {'caixas': caixas})



###################################################################################################
# Cadastro de Hospitais:
@login_required
def hospital_pesquisar(request):
        hospitais = Hospital.objects.all()
        return render(request, 'hospital/pesquisa.html', {'hospitais': hospitais})


def hospital_criar(request):
        if request.method == 'POST':
            form = HospitalForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
            return redirect('hospital_pesquisar')
        else:
            form = HospitalForm()
        return render(request, 'hospital/formulario.html', {'form': form})


def hospital_editar(request, pk):
        item = get_object_or_404(Hospital, pk=pk)
        if request.method == "POST":
            form = HospitalForm(request.POST, instance=item)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
            return redirect('hospital_pesquisar')
        else:
            form = HospitalForm(instance=item)
        return render(request, 'hospital/formulario.html', {'form': form})

def hospital_exportar(request):
        response = HttpResponse(content_type='text/csv')
        response ['Content-Disposition'] = 'attachment; filename = "Hospitais.csv"'
        writer = csv.writer(response)
        writer.writerow (['id', 'nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf', 'createdEm', 'createdPor'])
        hospitais = Hospital.objects.all().values_list( 'id', 'nome', 'telefone', 'nomeResponsavel', 'emailResponsavel', 'cep', 'logradouro', 'bairro', 'cidade', 'uf', 'createdEm', 'createdPor')
        for hospital in hospitais:
            writer.writerow(hospital)
        return response

def hospital_importar(request):
        hospitais = Hospital.objects.all()
        return render(request, 'hospital/pesquisa.html', {'hospitais': hospitais})

###################################################################################################
# Cadastro de Viagens:
@login_required
def viagem_pesquisar(request):
        viagens = Viagem.objects.all()
        return render(request, 'viagem/pesquisa.html', {'viagens': viagens})

def viagem_criar(request):
        if request.method == 'POST':
            form = ViagemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
            return redirect('viagem_pesquisar')
        else:
            form = ViagemForm()
        return render(request, 'viagem/formulario.html', {'form': form})

def viagem_editar(request, pk):
    item = get_object_or_404(Viagem, pk=pk)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=item)
        uploadform = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(pk, request.FILES['file'])
            item = form.save(commit=False)
            item.save()
            return redirect('viagem_pesquisar')
    else:
        uploadform = UploadFileForm()
        form = ViagemForm(instance=item)
    return render(request, 'viagem/formulario.html', {'form': form, 'uploadform': uploadform})

def viagem_exportar(request):
        response = HttpResponse(content_type='text/csv')
        response ['Content-Disposition'] = 'attachment; filename = "Viagens.csv"'
        writer = csv.writer(response)
        writer.writerow (['id', 'localPartida', 'localChegada', 'caixa', 'equipamento', 'nomeTransportador', 'contato', 'obs', 'createdEm', 'createdPor'])
        viagens = Viagem.objects.all().values_list( 'id', 'localPartida', 'localChegada', 'caixa', 'equipamento', 'nomeTransportador', 'contato', 'obs', 'createdEm', 'createdPor')
        for viagem in viagens:
            writer.writerow(viagem)
        return response

def viagem_importar(request):
        viagens = Viagem.objects.all()
        return render(request, 'viagem/pesquisa.html', {'viagens': viagens})

################################################################################
# Alteração de status
@login_required
def status_alterar(request, pk, cod):
    item = get_object_or_404(Viagem, pk=pk)
    item_status = Status.objects.get(codStatus = cod)
    item.status = item_status
    item.save()
    
    return JsonResponse({'result': 'ok', 'object':itemStatus.dscStatus})
    

###################################################################################################
# carrega página sobre a história e conceito do lifebox
@login_required
def sobre(request):
        return render(request, 'sobre/sobre.html')

###################################################################################################
# carrega página sobre a Equipe
@login_required
def equipe(request):
        return render(request, 'sobre/equipe.html')


###################################################################################################
# carrega página imprtar arquivos

@login_required
def importa(request):
        return render(request, 'importa/importa.html',)


@login_required
def importa_arquivo(request):
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'importa/importa.html', {'uploaded_file_url': uploaded_file_url})
        return render(request, 'importa/importa.html',)

###################################################################################################

###################################################################################################
# Upload de arquivos da viagem:
@login_required
def upload_file(request, pk):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(pk, request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload.html', {'uploadform': form})


def handle_uploaded_file(id, f):
    with open('uploas/viagens/viagem' + id + '.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
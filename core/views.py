# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse

from core.models import Equipamento, Caixa, Hospital, Viagem, Status
from core.forms import EquipamentoForm, CaixaForm, HospitalForm, ViagemForm

###################################################################################################
# Cadastro de Equipamentos:
@login_required
def equipamento_pesquisar(request): # Filtra os equipamentos:
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/pesquisa.html', {'equipamentosx': equipamentos})

@login_required
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

@login_required
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


###################################################################################################
# Cadastro de Caixas:
@login_required
def caixa_pesquisar(request):
    caixas = Caixa.objects.all()
    return render(request, 'caixa/pesquisa.html', {'caixas': caixas})

@login_required
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


@login_required
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

###################################################################################################
# Cadastro de Hospitais:
@login_required
def hospital_pesquisar(request):
        hospitais = Hospital.objects.all()
        return render(request, 'hospital/pesquisa.html', {'hospitais': hospitais})

@login_required
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

@login_required
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

###################################################################################################
# Cadastro de Viagens:
@login_required
def viagem_pesquisar(request):
    viagens = Viagem.objects.all()
    return render(request, 'viagem/pesquisa.html', {'viagens': viagens})


@login_required
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

@login_required
def viagem_editar(request, pk):
    item = get_object_or_404(Viagem, pk=pk)
    if request.method == "POST":
        form = ViagemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('viagem_pesquisar')
    else:
        form = ViagemForm(instance=item)
    return render(request, 'viagem/formulario.html', {'form': form})


################################################################################
# Alteração de status
def status_alterar(request, pk, cod):
    item = get_object_or_404(Viagem, pk=pk)
    item_status = Status.objects.get(codStatus = cod)

    print(item_status.dscStatus)

    item.status = item_status
    item.save()

    return JsonResponse({'result': 'ok', 'object':item_status.dscStatus})


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

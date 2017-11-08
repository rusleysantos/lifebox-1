from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.conf import settings

###################################################################################################
# modolo de monitoramento
@login_required
def mapas(request):
    return render(request, 'maps.html')

@login_required
def mapaplayback(request, pk):
    return render(request, 'example_1.html')
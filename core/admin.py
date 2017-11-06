# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Equipamento, Caixa, Hospital, Viagem, Status, Detalhe

class DetalheAdmin(admin.ModelAdmin):
    list_display = ('id','numLongitudeDeta', 'numLatitudeDeta', 'numTemperaturaDeta')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','codStatus', 'dscStatus')

admin.site.register(Equipamento)
admin.site.register(Caixa)
admin.site.register(Hospital)
admin.site.register(Viagem)
admin.site.register(Status, StatusAdmin)
admin.site.register(Detalhe, DetalheAdmin)
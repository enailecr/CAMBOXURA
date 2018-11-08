from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NumeroEntrada
from destinos.models import Destino
from uras.models import URA
from anuncios.models import Anuncio, Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo
from condicoestempo.models import CondicaoTempo
from troncos.models import Tronco
from destinos.forms import DestinoForm
from django.contrib.auth.decorators import login_required
import re
from django_tables2 import RequestConfig
from .tables import NumeroTable
import sys

@login_required
def add(request):
    data = {}
    dest_anuncios = Anuncio.objects.all()
    dest_gravacoes = Gravacao.objects.all()
    dest_numeros = NumeroEntrada.objects.all()
    dest_uras = URA.objects.all()
    dest_filas = Fila.objects.all()
    dest_chamadasGrupo = ChamadaEmGrupo.objects.all()
    dest_condicoes = CondicaoTempo.objects.all()
    dest_troncos = Tronco.objects.all()
    data['dest_anuncios'] = dest_anuncios
    data['dest_gravacoes'] = dest_gravacoes
    data['dest_numeros'] = dest_numeros
    data['dest_uras'] = dest_uras
    data['dest_filas'] = dest_filas
    data['dest_chamadasGrupo'] = dest_chamadasGrupo
    data['dest_condicoes'] = dest_condicoes
    data['dest_troncos'] = dest_troncos

    return render(request, 'CadastroNumero.html', data)

@login_required
def list(request):
    table = NumeroTable(NumeroEntrada.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'num.html', {'table': table})

# @login_required
# def dispositivo_busca(request):
#     dispositivos = Dispositivo.objects.all()
#     filter = request.GET.get('search')
#     if filter:
#         disp = []
#         for dispositivo in dispositivos:
#             if re.search(filter, dispositivo.unidade.sigla, re.IGNORECASE):
#                 disp.append(dispositivo)
#         dispositivos = disp
#     table = DispositivoTable(dispositivos)
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#     return render(request, 'menu-3d.html', {'table': table})

@login_required
def numero_novo(request):
    numero = request.POST['numero']
    origem = request.POST['origem']
    if 'atendido' in request.POST:
        atendido = request.POST['atendido']
    else:
        atendido = False
    if 'grava_chamada' in request.POST:
        gravaChamada = request.POST['grava_chamada']
    else:
        gravaChamada = False

    if 'dest_anuncios' in request.POST:
        destinoId = request.POST['dest_anuncios']

    if 'dest_gravacoes' in request.POST:
        destinoId = request.POST['dest_gravacoes']

    if 'dest_numeros' in request.POST:
        destinoId = request.POST['dest_numeros']

    if 'dest_uras' in request.POST:
        destinoId = request.POST['dest_uras']

    if 'dest_filas' in request.POST:
        destinoId = request.POST['dest_filas']

    if 'dest_chamadasGrupo' in request.POST:
        destinoId = request.POST['dest_chamadasGrupo']

    if 'dest_condicoes' in request.POST:
        destinoId = request.POST['dest_condicoes']

    if 'dest_troncos' in request.POST:
        destinoId = request.POST['dest_troncos']

    destino = Destino.objects.get(id=destinoId)

    numeroEntrada = NumeroEntrada(numero=numero, origem = origem, atendido=atendido, gravaChamada=gravaChamada, destino=destino)

    # form = NumeroEntradaForm(request.POST or None)
    # if form.is_valid():
    numeroEntrada.save()
    return redirect ('/numeros/')

@login_required
def numero_edita(request, id):
    data = {}

    numero = NumeroEntrada.objects.get(id=id)
    data['numero'] = numero
    if request.method == 'POST':
        numero = NumeroEntrada.objects.get(id=id)
        origem = request.POST['origem']
        if 'atendido' in request.POST:
                atendido = request.POST['atendido']
        else:
                atendido = False
        if 'grava_chamada' in request.POST:
                gravaChamada = request.POST['grava_chamada']
        else:
                gravaChamada = False

        numero.origem = origem
        numero.atendido = atendido
        numero.gravaChamada = gravaChamada
        numero.save()
        return redirect('/numeros/')

    else:
        return render(request, 'editaNumero.html', data)

@login_required
def numero_remove(request, id):
    numero = NumeroEntrada.objects.get(id=id)
    numero.delete()
    return redirect('/numeros/')

def carregaDestinos(request):
    tipoDesId = request.GET.get('tipo_des')
    destinos = Destinos.objects.filter(tipo=tipoDesId).order_by('tipo')
    return render(request, 'CadastroNumero.html', {'destinos': destinos})

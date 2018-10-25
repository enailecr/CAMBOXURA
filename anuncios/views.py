from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Anuncio 
import re
from django_tables2 import RequestConfig
from .tables import AnuncioTable

@login_required
def add(request):
    return render(request, 'CadastroAnuncio.html', data)

@login_required
def list(request):
    table = AnuncioTable(Anuncio.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'anuncios.html',{'table': table})

@login_required
def anuncio_novo(request):
    descricao = request.POST['descricao']
    repeticao = request.POST['repeticao']
    if 'pular' in request.POST: 
        pula = request.POST['pular']
    else:
        pula = False
    if 'retorna' in request.POST:   
        retornaURA = request.POST['retorna']
    else:
        retornaURA = False
    if 'resposta' in request.POST:   
        canalNaoResp = request.POST['resposta']
    else:
        canalNaoResp = False
    #destino = request.POST['nome']

    anuncio = Anuncio(descricao=descricao, repeticao = repeticao, pula=pular, retornaURA=retorna, canalNaoResp=resposta)
    anuncio.save()
    return redirect ('/anuncios/')
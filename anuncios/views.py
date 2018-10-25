from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Anuncio 
import re
from django_tables2 import RequestConfig
from .tables import AnuncioTable

@login_required
def add(request):
    return render(request, 'CadastroAnuncio.html')

@login_required
def list(request):
    table = AnuncioTable(Anuncio.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'anuncios.html',{'table': table})

@login_required
def anuncio_novo(request):
    descricao = request.POST['descricao']
    # repeticao = request.POST['repeticao']
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
    #destino = request.POST['nome']   repeticao = repeticao,
    anuncio = Anuncio(descricao=descricao, pula=pula,retornaURA=retornaURA, canalNaoResp=canalNaoResp )
    anuncio.save()
    return redirect ('/anuncios/')


@login_required
def anuncio_edita(request, id):
    data = {}
    anuncio = Anuncio.objects.get(id=id)
    data['anuncio'] = anuncio
    if request.method == 'POST':
        anuncio = Anuncio.objects.get(id=id)
        descricao = request.POST['descricao']
        # repeticao = request.POST['repeticao']
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
        
        anuncio.descricao = descricao
        #anuncio.repeticao = repeticao
        anuncio.pula = pula
        anuncio.retornaURA = retornaURA
        anuncio.canalNaoResp = canalNaoResp
        anuncio.save()        
        return redirect('/anuncios/')
    else:
        return render(request, 'editaAnuncio.html', data)

@login_required
def anuncio_remove(request, id):
    anuncio = Anuncio.objects.get(id=id)
    anuncio.delete()
    return redirect('/anuncios/')

from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Anuncio , Gravacao
import re
from django_tables2 import RequestConfig
from .tables import AnuncioTable
from django.conf import settings
from django.core.files.storage import FileSystemStorage

@login_required
def add(request):
    gravacoes = Gravacao.objects.all()
    return render(request, 'CadastroAnuncio.html', {'gravacoes': gravacoes})

@login_required
def list(request):
    table = AnuncioTable(Anuncio.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'anuncios.html',{'table': table})

@login_required
def anuncio_novo(request):
    descricao = request.POST['descricao']
    gravacaoId = request.POST['gravacao']
    gravacao = Gravacao.objects.get(id=gravacaoId)
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
    #destino = request.POST['nome']   repeticao = repeticao,
    anuncio = Anuncio(descricao=descricao, gravacaoAn=gravacao, repeticao=repeticao, pula=pula,retornaURA=retornaURA, canalNaoResp=canalNaoResp )
    anuncio.save()
    return redirect ('/anuncios/')


@login_required
def anuncio_edita(request, id):
    data = {}
    anuncio = Anuncio.objects.get(id=id)
    data['anuncio'] = anuncio
    if request.method == 'POST':
        descricao = request.POST['descricao']
        gravacaoId = request.POST['gravacao']
        gravacao = Gravacao.objects.get(id=gravacaoId)
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

        anuncio.descricao = descricao
        anuncio.repeticao = repeticao
        anuncio.gravacao = gravacao
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

@login_required
def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES['anexGravacao']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        nome = request.POST['nomeGravacao']
        gravacao = Gravacao(nome=nome, link=uploaded_file_url)
        gravacao.save()
        gravacoes = Gravacao.objects.all()
        data = {}
        data['gravacao'] = gravacao
        data['gravacoes'] = gravacoes
        return render(request, 'CadastroAnuncio.html', data)

from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Anuncio , Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo
from condicoestempo.models import CondicaoTempo
from troncos.models import Tronco
import re
from django_tables2 import RequestConfig
from .tables import AnuncioTable
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from logs.models import Log

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
    gravacoes = Gravacao.objects.exclude(musica__isnull=False)
    data['dest_anuncios'] = dest_anuncios
    data['dest_gravacoes'] = dest_gravacoes
    data['dest_numeros'] = dest_numeros
    data['dest_uras'] = dest_uras
    data['dest_filas'] = dest_filas
    data['dest_chamadasGrupo'] = dest_chamadasGrupo
    data['dest_condicoes'] = dest_condicoes
    data['dest_troncos'] = dest_troncos
    data['gravacoes'] = gravacoes
    return render(request, 'CadastroAnuncio.html', data)

@login_required
def list(request):
    table = AnuncioTable(Anuncio.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'anuncios.html',{'table': table})

@login_required
def anuncio_novo(request):
    descricao = request.POST['descricao']
    gravacaoId = request.POST['gravacao']
    if gravacaoId == '0' :
        gravacao = None
    else:
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

    if 'dest_anuncios' in request.POST:
        dest_anuncios = request.POST['dest_anuncios']

    if 'dest_gravacoes' in request.POST:
        dest_gravacoes = request.POST['dest_gravacoes']

    if 'dest_numeros' in request.POST:
        dest_numeros = request.POST['dest_numeros']

    if 'dest_uras' in request.POST:
        dest_uras = request.POST['dest_uras']

    if 'dest_filas' in request.POST:
        dest_filas = request.POST['dest_filas']

    if 'dest_chamadasGrupo' in request.POST:
        dest_chamadasGrupo = request.POST['dest_chamadasGrupo']

    if 'dest_condicoes' in request.POST:
        dest_condicoes = request.POST['dest_condicoes']

    if 'dest_troncos' in request.POST:
        dest_troncos = request.POST['dest_troncos']

    destinoId = 0
    if dest_anuncios != '0':
        destinoId = dest_anuncios
    if dest_gravacoes != '0':
        destinoId = dest_gravacoes
    if dest_numeros != '0':
        destinoId = dest_numeros
    if dest_uras != '0':
        destinoId = dest_uras
    if dest_filas != '0':
        destinoId = dest_filas
    if dest_chamadasGrupo != '0':
        destinoId = dest_chamadasGrupo
    if dest_condicoes != '0':
        destinoId = dest_condicoes
    if dest_troncos != '0':
        destinoId = dest_troncos

    tipoDestino = request.POST['tipo_des']

    tipo = '1'
    anuncio = Anuncio(tipo=tipo,descricao=descricao, repeticao=repeticao, pula=pula,retornaURA=retornaURA, canalNaoResp=canalNaoResp, )
    if gravacao:
        anuncio.gravacaoAn=gravacao
    anuncio.save()

    if destinoId != 0:
        anuncio.destinoTipo = tipoDestino
        anuncio.destino = destinoId
        anuncio.save()

    texto = request.user.username + " adicionou o anúncio: " +anuncio.descricao
    log = Log(log= texto)
    log.save()

    return redirect ('/anuncios/')


@login_required
def anuncio_edita(request, id):
    data = {}
    anuncio = Anuncio.objects.get(id=id)
    data['anuncio'] = anuncio
    if request.method == 'POST':
        descricao = request.POST['descricao']
        gravacaoId = request.POST['gravacao']
        if gravacaoId == "0" :
            gravacao = None
        else:
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

        if 'dest_anuncios' in request.POST:
            dest_anuncios = request.POST['dest_anuncios']

        if 'dest_gravacoes' in request.POST:
            dest_gravacoes = request.POST['dest_gravacoes']

        if 'dest_numeros' in request.POST:
            dest_numeros = request.POST['dest_numeros']

        if 'dest_uras' in request.POST:
            dest_uras = request.POST['dest_uras']

        if 'dest_filas' in request.POST:
            dest_filas = request.POST['dest_filas']

        if 'dest_chamadasGrupo' in request.POST:
            dest_chamadasGrupo = request.POST['dest_chamadasGrupo']

        if 'dest_condicoes' in request.POST:
            dest_condicoes = request.POST['dest_condicoes']

        if 'dest_troncos' in request.POST:
                dest_troncos = request.POST['dest_troncos']

        destinoId = 0
        if dest_anuncios != '0':
            destinoId = dest_anuncios
        if dest_gravacoes != '0':
            destinoId = dest_gravacoes
        if dest_numeros != '0':
            destinoId = dest_numeros
        if dest_uras != '0':
            destinoId = dest_uras
        if dest_filas != '0':
            destinoId = dest_filas
        if dest_chamadasGrupo != '0':
            destinoId = dest_chamadasGrupo
        if dest_condicoes != '0':
            destinoId = dest_condicoes
        if dest_troncos != '0':
            destinoId = dest_troncos

        tipoDestino = request.POST['tipo_des']

        if destinoId != 0:
            anuncio.destinoTipo = tipoDestino
            anuncio.destino = destinoId

        anuncio.descricao = descricao
        anuncio.repeticao = repeticao
        anuncio.gravacaoAn = gravacao
        anuncio.pula = pula
        anuncio.retornaURA = retornaURA
        anuncio.canalNaoResp = canalNaoResp
        anuncio.save()

        texto = request.user.username + " editou o anúncio: " +anuncio.descricao
        log = Log(log= texto)
        log.save()

        return redirect('/anuncios/')
    else:
        gravacoes = Gravacao.objects.exclude(musica__isnull=False)
        if anuncio.gravacaoAn :
            gravacao = anuncio.gravacaoAn
        else:
            gravacao = None
        data['gravacoes'] = gravacoes
        data['gravacao'] = gravacao

        dest_anuncios = Anuncio.objects.all()
        dest_gravacoes = Gravacao.objects.all()
        dest_numeros = NumeroEntrada.objects.all()
        dest_uras = URA.objects.all()
        dest_filas = Fila.objects.all()
        dest_chamadasGrupo = ChamadaEmGrupo.objects.all()
        dest_condicoes = CondicaoTempo.objects.all()
        dest_troncos = Tronco.objects.all()
        gravacoes = Gravacao.objects.exclude(musica__isnull=False)
        data['dest_anuncios'] = dest_anuncios
        data['dest_gravacoes'] = dest_gravacoes
        data['dest_numeros'] = dest_numeros
        data['dest_uras'] = dest_uras
        data['dest_filas'] = dest_filas
        data['dest_chamadasGrupo'] = dest_chamadasGrupo
        data['dest_condicoes'] = dest_condicoes
        data['dest_troncos'] = dest_troncos

        return render(request, 'editaAnuncio.html', data)

@login_required
def anuncio_remove(request, id):
    anuncio = Anuncio.objects.get(id=id)
    nome = anuncio.descricao
    anuncio.delete()
    texto = request.user.username + " removeu o anúncio: " +nome
    log = Log(log= texto)
    log.save()
    return redirect('/anuncios/')

@login_required
def upload_file_cad(request):
    if request.method == 'POST':
        myfile = request.FILES['anexGravacao']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        nome = request.POST['nomeGravacao']
        tipo = '2'
        gravacao = Gravacao(nome=nome, link=uploaded_file_url, tipo=tipo)
        gravacao.save()

        texto = request.user.username + ": adicionou a gravação: " +nome
        log = Log(log= texto)
        log.save()

        gravacoes = Gravacao.objects.exclude(musica__isnull=False)
        data = {}
        data['gravacao'] = gravacao
        data['gravacoes'] = gravacoes
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
        return render(request, 'CadastroAnuncio.html', data)

@login_required
def upload_file_edt(request, id):
    if request.method == 'POST':
        myfile = request.FILES['anexGravacao']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        tipo = '2'
        nome = request.POST['nomeGravacao']
        gravacao = Gravacao(nome=nome, link=uploaded_file_url, tipo=tipo)
        gravacao.save()
        gravacoes = Gravacao.objects.exclude(musica__isnull=False)
        data = {}
        anuncio = Anuncio.objects.get(id=id)
        data['anuncio'] = anuncio

        data['gravacao'] = gravacao
        data['gravacoes'] = gravacoes
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
        return render(request, 'editaAnuncio.html', data)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import URA, OpcaoURA
from anuncios.models import Anuncio, Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo
from condicoestempo.models import CondicaoTempo
from troncos.models import Tronco

import re
from django_tables2 import RequestConfig
from .tables import URATable
from logs.models import Log

@login_required
def add(request):
    anuncios = Anuncio.objects.all()
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
    data['anuncios'] = anuncios
    return render(request, 'UraNovo.html',data)

@login_required
def list(request):
    table = URATable(URA.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'uras.html', {'table': table})

@login_required
def ura_novo(request):
    nome = request.POST['nome_ura']
    descricao = request.POST['descricao']
    anuncioUra = request.POST['anuncio']
    discarDireto = request.POST['discar_direto']
    timeout = request.POST['timeout']
    tentativasInvalidas = request.POST['tent_inv']
    gravRepetInvalid = request.POST['invrerecor']

    if 'app_ann_inv' in request.POST:
        anexAnuncInvalid = request.POST['app_ann_inv']
    else:
        anexAnuncInvalid = False

    if 'ReturnInvalid' in request.POST:
        returnInvalid = request.POST['ReturnInvalid']
    else:
        returnInvalid = False

    gravInvalid =request.POST['gravinvalid']

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

    if 'ndest_anuncios' in request.POST:
        ndest_anuncios = request.POST['ndest_anuncios']

    if 'ndest_gravacoes' in request.POST:
        ndest_gravacoes = request.POST['ndest_gravacoes']

    if 'ndest_numeros' in request.POST:
        ndest_numeros = request.POST['ndest_numeros']

    if 'ndest_uras' in request.POST:
        ndest_uras = request.POST['ndest_uras']

    if 'ndest_filas' in request.POST:
        ndest_filas = request.POST['ndest_filas']

    if 'ndest_chamadasGrupo' in request.POST:
        ndest_chamadasGrupo = request.POST['ndest_chamadasGrupo']

    if 'ndest_condicoes' in request.POST:
        ndest_condicoes = request.POST['ndest_condicoes']

    if 'ndest_troncos' in request.POST:
        ndest_troncos = request.POST['ndest_troncos']

    ndestinoId = 0
    if ndest_anuncios != '0':
        ndestinoId = ndest_anuncios
    if ndest_gravacoes != '0':
        ndestinoId = ndest_gravacoes
    if ndest_numeros != '0':
        ndestinoId = ndest_numeros
    if ndest_uras != '0':
        ndestinoId = ndest_uras
    if ndest_filas != '0':
        ndestinoId = ndest_filas
    if ndest_chamadasGrupo != '0':
        ndestinoId = ndest_chamadasGrupo
    if ndest_condicoes != '0':
        ndestinoId = ndest_condicoes
    if ndest_troncos != '0':
        ndestinoId = ndest_troncos

    ntipoDestino = request.POST['ntipo_des']

    retentativasTimeout = request.POST['timeout_ret']
    gravRetentTimeout = request.POST['ret_tempo_esg']

    if 'append_anon_timout' in request.POST:
        anexAnuncTimeout = request.POST['append_anon_timout']
    else:
        anexAnuncTimeout = False

    if 'return_timout' in request.POST:
        retornarTimeout = request.POST['return_timout']
    else:
        retornarTimeout = False

    gravTimeout = request.POST['timeout_record']
    if 'append_anon_timout' in request.POST:
        returnURACaixaPostal = request.POST['append_anon_timout']
    else:
        returnURACaixaPostal = False

    tipo = '4'
    ura = URA(nome=nome,descricao=descricao,discarDireto=discarDireto,
    timeout=timeout,
    anexAnuncInvalid=anexAnuncInvalid,returnInvalid=returnInvalid,
    anexAnuncTimeout=anexAnuncTimeout,retornarTimeout=retornarTimeout,
    returnURACaixaPostal=returnURACaixaPostal, tipo=tipo)
    ura.save()

    if tentativasInvalidas != "dis":
        ura.tentativasInvalidas=tentativasInvalidas
        ura.save()

    if retentativasTimeout != "dis":
        ura.retentativasTimeout = retentativasTimeout
        ura.save()

    if destinoId != 0:
        ura.destinoInvalidTipo = tipoDestino
        ura.destinoInvalid = destinoId
        ura.save()

    if ndestinoId != 0:
        ura.destinoTimeoutTipo = ntipoDestino
        ura.destinoTimeout = ndestinoId
        ura.save()

    if anuncioUra !="0":
        anuncio = Anuncio.objects.get(id=anuncioUra)
        ura.anuncioUra = anuncio
        ura.save()

    if gravRetentTimeout != "0":
        gravacao = Gravacao.objects.get(id=gravRetentTimeout)
        ura.gravRetentTimeout = gravacao
        ura.save()

    if gravRepetInvalid != "0":
        gravacao = Gravacao.objects.get(id=gravRepetInvalid)
        ura.gravRepetInvalid = gravacao
        ura.save()

    if gravInvalid !="0":
        gravacao = Gravacao.objects.get(id=gravInvalid)
        ura.gravInvalid = gravacao
        ura.save()

    if gravTimeout !="0":
        gravacao = Gravacao.objects.get(id=gravTimeout)
        ura.gravTimeout = gravacao
        ura.save()

    tipoDestino = []
    dest_anuncios = []
    dest_gravacoes = []
    dest_numeros = []
    dest_uras = []
    dest_filas = []
    dest_chamadasGrupo = []
    dest_condicoes = []
    dest_troncos = []
    ramal = []
    retornar = []

    contador = int(request.POST['count'])
    for i in range(contador):
        ramal.append(request.POST['ramal'+str(i)])
        tipoDestino.append(request.POST['tipo_des'+str(i)])
        dest_anuncios.append(request.POST['dest_anuncios'+str(i)])
        dest_gravacoes.append(request.POST['dest_gravacoes'+str(i)])
        dest_numeros.append(request.POST['dest_numeros'+str(i)])
        dest_uras.append(request.POST['dest_uras'+str(i)])
        dest_filas.append(request.POST['dest_filas'+str(i)])
        dest_chamadasGrupo.append(request.POST['dest_chamadasGrupo'+str(i)])
        dest_condicoes.append(request.POST['dest_condicoes'+str(i)])
        dest_troncos.append(request.POST['dest_troncos'+str(i)])
        retorna = 'retornar' + str(i)
        if retorna in request.POST:
            retornar.append(True)
        else:
            retornar.append(False)

    cont=0;
    while cont < contador:
        if tipoDestino[cont] == '1':
            destino = dest_anuncios[cont]
        if tipoDestino[cont] == '2':
            destino = dest_gravacoes[cont]
        if tipoDestino[cont] == '3':
            destino = dest_numeros[cont]
        if tipoDestino[cont] == '4':
            destino = dest_uras[cont]
        if tipoDestino[cont] == '5':
            destino = dest_filas[cont]
        if tipoDestino[cont] == '6':
            destino = dest_chamadasGrupo[cont]
        if tipoDestino[cont] == '7':
            destino = dest_condicoes[cont]
        if tipoDestino[cont] == '8':
            destino = dest_troncos[cont]

        if destino:
            opcaoURA = OpcaoURA(ura = ura,tipoDestino = tipoDestino[cont],destino = destino, ramal=ramal[cont], retornar=retornar[cont])
            opcaoURA.save()
        cont= cont + 1

    texto = request.user.username + " adicionou a URA: " +nome
    log = Log(log= texto)
    log.save()

    return redirect ('/uras/')


@login_required
def ura_edita(request, id):
    data = {}
    ura = URA.objects.get(id=id)
    data['ura'] = ura
    if request.method == 'POST':
        nome = request.POST['nome_ura']
        descricao = request.POST['descricao']
        anuncioUra = request.POST['anuncio']
        discarDireto = request.POST['discar_direto']
        timeout = request.POST['timeout']
        tentativasInvalidas = request.POST['tent_inv']
        gravRepetInvalid = request.POST['invrerecor']

        if 'app_ann_inv' in request.POST:
            anexAnuncInvalid = request.POST['app_ann_inv']
        else:
            anexAnuncInvalid = False

        if 'ReturnInvalid' in request.POST:
            returnInvalid = request.POST['ReturnInvalid']
        else:
            returnInvalid = False

        gravInvalid =request.POST['gravinvalid']

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

        if 'ndest_anuncios' in request.POST:
            ndest_anuncios = request.POST['ndest_anuncios']

        if 'ndest_gravacoes' in request.POST:
            ndest_gravacoes = request.POST['ndest_gravacoes']

        if 'ndest_numeros' in request.POST:
            ndest_numeros = request.POST['ndest_numeros']

        if 'ndest_uras' in request.POST:
            ndest_uras = request.POST['ndest_uras']

        if 'ndest_filas' in request.POST:
            ndest_filas = request.POST['ndest_filas']

        if 'ndest_chamadasGrupo' in request.POST:
            ndest_chamadasGrupo = request.POST['ndest_chamadasGrupo']

        if 'ndest_condicoes' in request.POST:
            ndest_condicoes = request.POST['ndest_condicoes']

        if 'ndest_troncos' in request.POST:
            ndest_troncos = request.POST['ndest_troncos']

        ndestinoId = 0
        if ndest_anuncios != '0':
            ndestinoId = ndest_anuncios
        if ndest_gravacoes != '0':
            ndestinoId = ndest_gravacoes
        if ndest_numeros != '0':
            ndestinoId = ndest_numeros
        if ndest_uras != '0':
            ndestinoId = ndest_uras
        if ndest_filas != '0':
            ndestinoId = ndest_filas
        if ndest_chamadasGrupo != '0':
            ndestinoId = ndest_chamadasGrupo
        if ndest_condicoes != '0':
            ndestinoId = ndest_condicoes
        if ndest_troncos != '0':
            ndestinoId = ndest_troncos

        ntipoDestino = request.POST['ntipo_des']

        retentativasTimeout = request.POST['timeout_ret']
        gravRetentTimeout = request.POST['ret_tempo_esg']

        if 'append_anon_timout' in request.POST:
            anexAnuncTimeout = request.POST['append_anon_timout']
        else:
            anexAnuncTimeout = False

        if 'return_timout' in request.POST:
            retornarTimeout = request.POST['return_timout']
        else:
            retornarTimeout = False

        gravTimeout = request.POST['timeout_record']
        if 'append_anon_timout' in request.POST:
            returnURACaixaPostal = request.POST['append_anon_timout']
        else:
            returnURACaixaPostal = False

        ura.nome=nome
        ura.descricao=descricao
        ura.discarDireto=discarDireto
        ura.timeout=timeout
        ura.anexAnuncInvalid=anexAnuncInvalid
        ura.returnInvalid=returnInvalid
        ura.anexAnuncTimeout=anexAnuncTimeout
        ura.retornarTimeout=retornarTimeout
        ura.returnURACaixaPostal=returnURACaixaPostal
        ura.save()

        if tentativasInvalidas != "dis":
            ura.tentativasInvalidas=tentativasInvalidas
            ura.save()
        else:
            ura.tentativasInvalidas=None
            ura.save()

        if retentativasTimeout != "dis":
            ura.retentativasTimeout = retentativasTimeout
            ura.save()
        else:
            ura.retentativasTimeout=None
            ura.save()

        if destinoId != 0:
            ura.destinoInvalidTipo = tipoDestino
            ura.destinoInvalid = destinoId
            ura.save()

        if ndestinoId != 0:
            ura.destinoTimeoutTipo = ntipoDestino
            ura.destinoTimeout = ndestinoId
            ura.save()

        if anuncioUra != "0":
            anuncio = Anuncio.objects.get(id=anuncioUra)
            ura.anuncioUra = anuncio
            ura.save()
        else:
            ura.anuncioUra = None
            ura.save()

        if gravRetentTimeout != "0":
            gravacao = Gravacao.objects.get(id=gravRetentTimeout)
            ura.gravRetentTimeout = gravacao
            ura.save()
        else:
            ura.gravRetentTimeout = None
            ura.save()

        if gravRepetInvalid != "0":
            gravacao = Gravacao.objects.get(id=gravRepetInvalid)
            ura.gravRepetInvalid = gravacao
            ura.save()
        else:
            ura.gravRepetInvalid = None
            ura.save()

        if gravInvalid !="0":
            gravacao = Gravacao.objects.get(id=gravInvalid)
            ura.gravInvalid = gravacao
            ura.save()
        else:
            ura.gravInvalid = None
            ura.save()

        if gravTimeout !="0":
            gravacao = Gravacao.objects.get(id=gravTimeout)
            ura.gravTimeout = gravacao
            ura.save()
        else:
            ura.gravTimeout = None
            ura.save()

        texto = request.user.username + " editou a URA: " +nome
        log = Log(log= texto)
        log.save()

        return redirect('/uras/')
    else:
        anuncios = Anuncio.objects.all()
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
        data['anuncios'] = anuncios
        return render(request, 'editaUra.html', data)


@login_required
def ura_remove(request, id):
    ura = URA.objects.get(id=id)
    nome = ura.nome
    ura.delete()
    texto = request.user.username + " removeu a URA: " +nome
    log = Log(log= texto)
    log.save()
    return redirect('/uras/')

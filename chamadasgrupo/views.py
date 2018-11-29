from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from musicas.models import MusicaCategoria, Musica
from uras.models import URA
from anuncios.models import Anuncio, Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo, ListaExtensao
from condicoestempo.models import CondicaoTempo
from troncos.models import Tronco
import re
from django_tables2 import RequestConfig
from .tables import ChamadaEmGrupoTable
from logs.models import Log

@login_required
def add(request):
    anuncios = Anuncio.objects.all()
    musicas = Musica.objects.all()
    data={}
    data['anuncios'] = anuncios
    data['musicas'] = musicas
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
    return render(request, 'CadastroChamadasGrupo.html',data)

@login_required
def list(request):
    table = ChamadaEmGrupoTable(ChamadaEmGrupo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'ringGroup.html',{'table': table})

@login_required
def chamadasgrupo_novo(request):
    descricao = request.POST['descricao']
    estrategia = request.POST['estrategia']
    tempoChamada = request.POST['tempoChamada']
    anuncioCGID = request.POST['anuncioCG']
    if anuncioCGID == "0" :
        anuncioCG = None
    else:
        anuncioCG = Anuncio.objects.get(id=anuncioCGID)
    #musicaEspera = request.POST['musicaEspera']
    musicasID = request.POST['musicaEspera']
    if musicasID == "0" :
        musicas = None
    else:
        musicas = Musica.objects.get(id=musicasID)
    prefixCID = request.POST['prefixCID']
    infoAlerta = request.POST['infoAlerta']
    #anuncioRemoto
    anuncioRemotoID = request.POST['anuncioRemoto']
    if anuncioRemotoID == "0" :
        anuncioRemoto = None
    else:
        anuncioRemoto = Anuncio.objects.get(id=anuncioRemotoID)
    #anuncioTardio
    anuncioTardioID = request.POST['anuncioTardio']
    if anuncioTardioID == "0" :
        anuncioTardio = None
    else:
        anuncioTardio = Anuncio.objects.get(id=anuncioTardioID)
    modo = request.POST['modo']
    valorFixoCID = request.POST['valorFixoCID']
    gravarChamadas = request.POST['gravarChamadas']

    if 'igConfigCF' in request.POST:
        igConfigCF = request.POST['igConfigCF']
    else:
        igConfigCF = False

    if 'igAgentOcupado' in request.POST:
        igAgentOcupado = request.POST['igAgentOcupado']
    else:
        igAgentOcupado = False

    if 'atendeChamada' in request.POST:
        atendeChamada = request.POST['atendeChamada']
    else:
        atendeChamada = False

    if 'confirm_chamada' in request.POST:
        confirmaChamada = request.POST['confirm_chamada']
    else:
        confirmaChamada = False

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

    tipo = '6'
    chamadasgrupo = ChamadaEmGrupo(descricao=descricao, gravarChamadas=gravarChamadas, modo=modo , estrategia=estrategia, tempoChamada=tempoChamada, prefixCID=prefixCID, infoAlerta=infoAlerta,valorFixoCID=valorFixoCID,
    igConfigCF=igConfigCF,igAgentOcupado=igAgentOcupado, atendeChamada=atendeChamada,confirmaChamada=confirmaChamada, anuncioCG=anuncioCG,
    anuncioRemoto=anuncioRemoto,anuncioTardio=anuncioTardio, musicaEspera=musicas, tipo=tipo   )
    # musica = Musica( )
    chamadasgrupo.save()
    if destinoId != 0:
        chamadasgrupo.destinoTipo = tipoDestino
        chamadasgrupo.destino = destinoId
        chamadasgrupo.save()

    lista_area = request.POST['lista_ext']
    cont = 1
    lista = lista_area.splitlines()
    for linha in lista:
        lista = ListaExtensao(numero=linha, ordem=cont, chamada=chamadasgrupo)
        lista.save()
        cont = cont +1

    texto = request.user.username + " adicionou a chamada em grupo: " +descricao
    log = Log(log= texto)
    log.save()

    return redirect ('/chamadasgrupo/')

@login_required
def chamadasgrupo_edita(request, id):
    data = {}
    chamadasgrupo = ChamadaEmGrupo.objects.get(id=id)
    data['chamadasgrupo'] = chamadasgrupo
    if request.method == 'POST':
        chamadasgrupo = ChamadaEmGrupo.objects.get(id=id)

        descricao = request.POST['descricao']
        estrategia = request.POST['estrategia']
        tempoChamada = request.POST['tempoChamada']
        anuncioCGID = request.POST['anuncioCG']
        if anuncioCGID == "0" :
            anuncioCG = None
        else:
            anuncioCG = Anuncio.objects.get(id=anuncioCGID)
        #musicaEspera = request.POST['musicaEspera']
        musicaEsperaID = request.POST['musicaEspera']
        if musicaEsperaID == "0" :
            musicaEspera = None
        else:
            musicaEspera = Musica.objects.get(id=musicaEsperaID)
        prefixCID = request.POST['prefixCID']
        infoAlerta = request.POST['infoAlerta']
        #anuncioRemoto
        anuncioRemotoID = request.POST['anuncioRemoto']
        if anuncioRemotoID == "0" :
            anuncioRemoto = None
        else:
            anuncioRemoto = Anuncio.objects.get(id=anuncioRemotoID)
        #anuncioTardio
        anuncioTardioID = request.POST['anuncioTardio']
        if anuncioTardioID == "0" :
            anuncioTardio = None
        else:
            anuncioTardio = Anuncio.objects.get(id=anuncioTardioID)
        modo = request.POST['modo']
        valorFixoCID = request.POST['valorFixoCID']
        gravarChamadas = request.POST['gravarChamadas']

        if 'igConfigCF' in request.POST:
            igConfigCF = request.POST['igConfigCF']
        else:
            igConfigCF = False

        if 'igAgentOcupado' in request.POST:
            igAgentOcupado = request.POST['igAgentOcupado']
        else:
            igAgentOcupado = False

        if 'atendeChamada' in request.POST:
            atendeChamada = request.POST['atendeChamada']
        else:
            atendeChamada = False

        if 'confirm_chamada' in request.POST:
            confirmaChamada = request.POST['confirm_chamada']
        else:
            confirmaChamada = False

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
            chamadasgrupo.destinoTipo = tipoDestino
            chamadasgrupo.destino = destinoId

        chamadasgrupo.descricao =descricao
        chamadasgrupo.estrategia = estrategia
        chamadasgrupo.tempoChamada = tempoChamada
        chamadasgrupo.anuncioCG = anuncioCG
        chamadasgrupo.musicaEspera = musicaEspera
        chamadasgrupo.prefixCID = prefixCID
        chamadasgrupo.infoAlerta = infoAlerta
        chamadasgrupo.anuncioRemoto = anuncioRemoto
        chamadasgrupo.anuncioTardio = anuncioTardio
        chamadasgrupo.modo = modo
        chamadasgrupo.valorFixoCID = valorFixoCID
        chamadasgrupo.gravarChamadas = gravarChamadas
        chamadasgrupo.igConfigCF = igConfigCF
        chamadasgrupo.igAgentOcupado = igAgentOcupado
        chamadasgrupo.atendeChamada = atendeChamada

        chamadasgrupo.confirmaChamada = confirmaChamada

        chamadasgrupo.save()

        listai = ListaExtensao.objects.filter(chamada=id)
        for item in listai:
            item.delete()

        lista_area = request.POST['lista_ext']
        cont = 1
        lista = lista_area.splitlines()
        for linha in lista:
            lin = linha.strip(" ")
            if lin != "":
                lista = ListaExtensao(numero=lin, ordem=cont, chamada=chamadasgrupo)
                lista.save()
                cont = cont +1

        texto = request.user.username + " editou a chamada em grupo: " +descricao
        log = Log(log= texto)
        log.save()

        return redirect('/chamadasgrupo/')
    else:
        anuncios = Anuncio.objects.all()
        musicas = Musica.objects.all()
        if chamadasgrupo.anuncioCG :
            anuncioCG = chamadasgrupo.anuncioCG
        else:
            anuncioCG = None
        if chamadasgrupo.anuncioRemoto :
            anuncioRemoto = chamadasgrupo.anuncioRemoto
        else:
            anuncioRemoto = None
        if chamadasgrupo.anuncioTardio :
            anuncioTardio = chamadasgrupo.anuncioTardio
        else:
            anuncioTardio = None

        if chamadasgrupo.musicaEspera :
            musicaEspera = chamadasgrupo.musicaEspera
        else:
            musicaEspera = None
        data['anuncios'] = anuncios
        data['musicas'] = musicas
        data['anuncioCG'] = anuncioCG
        data['anuncioRemoto'] = anuncioRemoto
        data['anuncioTardio'] = anuncioTardio
        data['musicaEspera'] = musicaEspera

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

        listai = ListaExtensao.objects.filter(chamada=id)
        lista = ""
        for num in listai:
            lista = lista+num.numero.strip() +"\n"
        data['lista'] = lista

        return render(request, 'editaChamadaEmGrupo.html', data)

@login_required
def chamadasgrupo_remove(request, id):
    chamadasgrupo = ChamadaEmGrupo.objects.get(id=id)
    cham = chamadasgrupo.descricao
    chamadasgrupo.delete()
    texto = request.user.username + ": removeu a chamada em grupo: " +cham
    log = Log(log= texto)
    log.save()

    return redirect('/chamadasgrupo/')

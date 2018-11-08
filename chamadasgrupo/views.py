from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import ChamadaEmGrupo, Anuncio, Musica
from musicas.models import MusicaCategoria
import re
from django_tables2 import RequestConfig
from .tables import ChamadaEmGrupoTable

@login_required
def add(request):
    anuncios = Anuncio.objects.all()
    musicas = Musica.objects.all()
    data={}
    data['anuncios'] = anuncios
    data['musicas'] = musicas
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

    #destino = request.POST['nome']
    tipo = '6'
    chamadasgrupo = ChamadaEmGrupo(descricao=descricao, gravarChamadas=gravarChamadas, modo=modo , estrategia=estrategia, tempoChamada=tempoChamada, prefixCID=prefixCID, infoAlerta=infoAlerta,valorFixoCID=valorFixoCID,
    igConfigCF=igConfigCF,igAgentOcupado=igAgentOcupado, atendeChamada=atendeChamada,confirmaChamada=confirmaChamada, anuncioCG=anuncioCG,
    anuncioRemoto=anuncioRemoto,anuncioTardio=anuncioTardio, musicaEspera=musicas, tipo=tipo   )
    # musica = Musica( )
    chamadasgrupo.save()
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
        #destino = request.POST['nome']   repeticao = repeticao,
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

        return render(request, 'editaChamadaEmGrupo.html', data)

@login_required
def chamadasgrupo_remove(request, id):
    chamadasgrupo = ChamadaEmGrupo.objects.get(id=id)
    chamadasgrupo.delete()
    return redirect('/chamadasgrupo/')

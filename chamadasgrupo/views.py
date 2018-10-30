from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import ChamadaEmGrupo, Anuncio, Musica
import re
from django_tables2 import RequestConfig
from .tables import ChamadaEmGrupoTable

@login_required
def add(request):
    return render(request, 'CadastroChamadasGrupo.html')

@login_required
def list(request):
    table = ChamadaEmGrupoTable(ChamadaEmGrupo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'ringGroup.html',{'table': table})

@login_required
def chamadasgrupo_novo(request):
    descricao = request.POST['descricao']
    #estrategia = request.POST['estrategia'] 
    tempoChamada = request.POST['tempoChamada']
    #anuncioCG = request.POST['anuncioCG']
    #musicaEspera = request.POST['musicaEspera']
    prefixCID = request.POST['prefixCID']
    infoAlerta = request.POST['infoAlerta']
    #anuncioRemoto = request.POST['anuncioRemoto']
    #anuncioTardio = request.POST['anuncioTardio']
    #modo = request.POST['modo']
    valorFixoCID = request.POST['valorFixoCID']
    #gravarChamadas = request.POST['gravarChamadas']

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

    #destino = request.POST['nome']   estrategia=estrategia, modo=modo ,gravarChamadas=gravarChamadas
    chamadasgrupo = ChamadaEmGrupo(descricao=descricao, tempoChamada=tempoChamada, prefixCID=prefixCID, infoAlerta=infoAlerta,valorFixoCID=valorFixoCID,
    igConfigCF=igConfigCF,igAgentOcupado=igAgentOcupado, atendeChamada=atendeChamada,confirmaChamada=confirmaChamada)
    #anuncio = Anuncio(anuncioRemoto=anuncioRemoto, anuncioCG=anuncioCG, anuncioTardio=anuncioTardio)
    #musica = Musica( musicaEspera=musicaEspera)
   # musica.save()
    chamadasgrupo.save()
    #anuncio.save()
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
        anuncioCG = request.POST['anuncioCG']
        musicaEspera = request.POST['musicaEspera']
        prefixCID = request.POST['prefixCID']
        infoAlerta = request.POST['infoAlerta']
        anuncioRemoto = request.POST['anuncioRemoto']
        anuncioTardio = request.POST['anuncioTardio']
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

        #destino = request.POST['nome']   repeticao = repeticao,
        
        chamadasgrupo.estrategia = estrategia
        chamadasgrupo.tempoChamada = tempoChamada
        # deve ser anuncio e nao chamadasgrupo.anuncioCG = anuncioCG
        #deve ser musica e nao chamadasgrupo.musicaEspera = musicaEspera
        chamadasgrupo.prefixCID = prefixCID
        chamadasgrupo.infoAlerta = infoAlerta
        # chamadasgrupo.anuncioRemoto = anuncioRemoto
        # chamadasgrupo.anuncioTardio = anuncioTardio
        chamadasgrupo.modo = modo
        chamadasgrupo.valorFixoCID = valorFixoCID
        chamadasgrupo.gravarChamadas = gravarChamadas
        chamadasgrupo.igConfigCF = igConfigCF
        chamadasgrupo.igAgentOcupado = igAgentOcupado
        chamadasgrupo.atendeChamada = atendeChamada

        chamadasgrupo.save()        
        return redirect('/chamadasgrupo/')
    else:
        return render(request, 'editaChamadaEmGrupo.html', data)

@login_required
def chamadasgrupo_remove(request, id):
    chamadasgrupo = ChamadaEmGrupo.objects.get(id=id)
    chamadasgrupo.delete()
    return redirect('/chamadasgrupo/')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tronco, TroncoSIP, TroncoIAX, TroncoCustomizado, RegraManipulaNum
import re
from django_tables2 import RequestConfig
from .tables import TroncoTable
from django.core.exceptions import ObjectDoesNotExist
from logs.models import Log

#TroncoSIP
@login_required
def addtroncosip(request):
    return render(request, 'CadastroTroncoSIP.html')

#TroncoIAX
@login_required
def addtroncoiax(request):
    return render(request, 'CadastroTroncoIAX.html')

#TroncoCustomizado
@login_required
def addtroncocustomizado(request):
    return render(request, 'CadastroTroncoCustomizado.html')


@login_required
def list(request):
    table = TroncoTable(Tronco.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'troncos.html', {'table': table})

#TroncoSIP
@login_required
def troncosip_novo(request):
    nome = request.POST['nome']
    callerIDSaida = request.POST['callerids']
    opcoesCID = request.POST['op_cid']
    maxCanais = request.POST['max_canais']
    opcoesDiskAsterisk = request.POST['op_asterisk']
    if 'continua_ocup' in request.POST:
        contSeOcup = request.POST['continua_ocup']
    else:
        contSeOcup = False

    if 'desab_tronco' in request.POST:
        desabTronco = request.POST['desab_tronco']
    else:
        desabTronco = False

    prefixChamSaida = request.POST['prefixo_saida']

    nomeTronco = request.POST['nome_tronco']
    detalhesPEER = request.POST['detalhes_PEER']
    contextoUsuario = request.POST['contexto']
    detalhesUsuario = request.POST['detalhes_usuarios']
    stringRegistro = request.POST['string_reg']

    tipo = '8'
    troncoSIP = TroncoSIP(tipo=tipo, nome=nome, opcoesCID=opcoesCID,contSeOcup=contSeOcup,desabTronco=desabTronco, prefixChamSaida=prefixChamSaida)
    troncoSIP.save()

    troncoSIP.callerIDSaida = callerIDSaida
    troncoSIP.maxCanais = maxCanais
    troncoSIP.opcoesDiskAsterisk = opcoesDiskAsterisk
    troncoSIP.nomeTronco = nomeTronco
    troncoSIP.detalhesPEER = detalhesPEER
    troncoSIP.contextoUsuario = contextoUsuario
    troncoSIP.detalhesUsuario = detalhesUsuario
    troncoSIP.stringRegistro = stringRegistro

    troncoSIP.save()

    precedente = []
    prefixo = []
    padraoEquiv = []

    contador = int(request.POST['count'])
    for i in range(contador):
        precedente.append(request.POST['precedente'+str(i)])
        prefixo.append(request.POST['prefix'+str(i)])
        padraoEquiv.append(request.POST['match'+str(i)])

    cont=0;
    while cont < contador:
        regramanip = RegraManipulaNum(precedente = precedente[cont],prefixo = prefixo[cont],padrao = padraoEquiv[cont], tronco=troncoSIP)
        regramanip.save()
        cont= cont + 1

    texto = request.user.username + " adicionou o tronco SIP: " +nome
    log = Log(log= texto)
    log.save()
    return redirect ('/troncos/')

#TroncoIAX
@login_required
def troncoiax_novo(request):
    nome = request.POST['nome']
    callerIDSaida = request.POST['callerids']
    opcoesCID = request.POST['op_cid']
    maxCanais = request.POST['max_canais']
    opcoesDiskAsterisk = request.POST['op_asterisk']
    if 'continua_ocup' in request.POST:
        contSeOcup = request.POST['continua_ocup']
    else:
        contSeOcup = False
    if 'desab_tronco' in request.POST:
        desabTronco = request.POST['desab_tronco']
    else:
        desabTronco = False
    prefixChamSaida = request.POST['prefixo_saida']

    nomeTronco = request.POST['nome_tronco']
    detalhesPEER = request.POST['detalhes_PEER']
    contextoUsuario = request.POST['contexto']
    detalhesUsuario = request.POST['detalhes_usuarios']
    stringRegistro = request.POST['string_reg']

    tipo = '8'
    troncoIAX = TroncoIAX(tipo=tipo, nome=nome, opcoesCID=opcoesCID,contSeOcup=contSeOcup,desabTronco=desabTronco, prefixChamSaida=prefixChamSaida)
    troncoIAX.save()

    troncoIAX.callerIDSaida = callerIDSaida
    troncoIAX.maxCanais = maxCanais
    troncoIAX.opcoesDiskAsterisk = opcoesDiskAsterisk
    troncoIAX.nomeTronco = nomeTronco
    troncoIAX.detalhesPEER = detalhesPEER
    troncoIAX.contextoUsuario = contextoUsuario
    troncoIAX.detalhesUsuario = detalhesUsuario
    troncoIAX.stringRegistro = stringRegistro
    troncoIAX.save()

    precedente = []
    prefixo = []
    padraoEquiv = []

    contador = int(request.POST['count'])
    for i in range(contador):
        precedente.append(request.POST['precedente'+str(i)])
        prefixo.append(request.POST['prefix'+str(i)])
        padraoEquiv.append(request.POST['match'+str(i)])

    cont=0;
    while cont < contador:
        regramanip = RegraManipulaNum(precedente = precedente[cont],prefixo = prefixo[cont],padrao = padraoEquiv[cont], tronco =troncoIAX)
        regramanip.save()
        cont= cont + 1

    texto = request.user.username + " adicionou o tronco IAX: " +nome
    log = Log(log= texto)
    log.save()

    return redirect ('/troncos/')

#TroncoCustomizado
@login_required
def troncocustomizado_novo(request):
    nome = request.POST['nome']
    callerIDSaida = request.POST['callerids']
    opcoesCID = request.POST['op_cid']
    maxCanais = request.POST['max_canais']
    opcoesDiskAsterisk = request.POST['op_asterisk']
    if 'continua_ocup' in request.POST:
        contSeOcup = request.POST['continua_ocup']
    else:
        contSeOcup = False
    if 'desab_tronco' in request.POST:
        desabTronco = request.POST['desab_tronco']
    else:
        desabTronco = False
    # precedente = request.POST['precedente']
    # prefixo = request.POST['prefix']
    # padraoEquiv = request.POST['match']
    prefixChamSaida = request.POST['prefixo_saida']

    stringChamada = request.POST['string_chamada']
    tipo = '8'
    troncoCustom = TroncoCustomizado(tipo=tipo,nome=nome, opcoesCID=opcoesCID,contSeOcup=contSeOcup,desabTronco=desabTronco, prefixChamSaida=prefixChamSaida)
    troncoCustom.save()

    troncoCustom.callerIDSaida = callerIDSaida
    troncoCustom.maxCanais = maxCanais
    troncoCustom.opcoesDiskAsterisk = opcoesDiskAsterisk
    troncoCustom.stringChamada = stringChamada

    troncoCustom.save()
    precedente = []
    prefixo = []
    padraoEquiv = []

    contador = int(request.POST['count'])
    for i in range(contador):
        precedente.append(request.POST['precedente'+str(i)])
        prefixo.append(request.POST['prefix'+str(i)])
        padraoEquiv.append(request.POST['match'+str(i)])

    cont=0;
    while cont < contador:
        regramanip = RegraManipulaNum(precedente = precedente[cont],prefixo = prefixo[cont],padrao = padraoEquiv[cont], tronco =troncoCustom)
        regramanip.save()
        cont= cont + 1

    texto = request.user.username + " adicionou o tronco customizado: " +nome
    log = Log(log= texto)
    log.save()

    return redirect ('/troncos/')

@login_required
def tronco_edita(request, id):
    data = {}
    tronco = Tronco.objects.get(id=id)
    data['tronco'] = tronco
    regra = RegraManipulaNum.objects.filter(tronco=tronco)
    count= len(regra)
    data['regra'] = regra
    data['count'] = count
    if request.method == 'POST':
        nome = request.POST['nome']
        callerIDSaida = request.POST['callerids']
        opcoesCID = request.POST['op_cid']
        maxCanais = request.POST['max_canais']
        opcoesDiskAsterisk = request.POST['op_asterisk']
        if 'continua_ocup' in request.POST:
            contSeOcup = request.POST['continua_ocup']
        else:
            contSeOcup = False
        if 'desab_tronco' in request.POST:
            desabTronco = request.POST['desab_tronco']
        else:
            desabTronco = False
        prefixChamSaida = request.POST['prefixo_saida']

        nomeTronco = request.POST['nome_tronco']
        detalhesPEER = request.POST['detalhes_PEER']
        contextoUsuario = request.POST['contexto']
        detalhesUsuario = request.POST['detalhes_usuarios']
        stringRegistro = request.POST['string_reg']

        precedente = []
        prefixo = []
        padraoEquiv = []

        tronco.nome = nome
        tronco.callerIDSaida = callerIDSaida
        tronco.opcoesCID = opcoesCID
        tronco.maxCanais = maxCanais
        tronco.opcoesDiskAsterisk = opcoesDiskAsterisk
        tronco.contSeOcup = contSeOcup
        tronco.desabTronco = desabTronco
        tronco.prefixChamSaida = prefixChamSaida
        tronco.nomeTronco = nomeTronco
        tronco.detalhesPEER = detalhesPEER
        tronco.contextoUsuario = contextoUsuario
        tronco.detalhesUsuario = detalhesUsuario
        tronco.stringRegistro = stringRegistro
        tronco.save()

        cont=0;
        for r in regra:
            r.delete()

        contador = int(request.POST['count'])
        conta= 0
        for i in range(contador):
            if request.POST['precedente'+str(i)]:
                precedente.append(request.POST['precedente'+str(i)])
                prefixo.append(request.POST['prefix'+str(i)])
                padraoEquiv.append(request.POST['match'+str(i)])
                conta = conta +1


        while cont < conta:
            regramanip = RegraManipulaNum(precedente = precedente[cont],prefixo = prefixo[cont],padrao = padraoEquiv[cont], tronco =tronco)
            regramanip.save()
            cont= cont + 1

        texto = request.user.username + " editou o tronco: " +tronco.nome
        log = Log(log= texto)
        log.save()

        return redirect('/troncos/')
    else:
        try:
            tronco = TroncoCustomizado.objects.get(id=id)
            return render(request, 'editaTroncoCustom.html', data)
        except TroncoCustomizado.DoesNotExist:
            return render(request, 'editaTronco.html', data)


@login_required
def tronco_remove(request, id):
    tronco = Tronco.objects.get(id=id)
    nome= tronco.nome
    tronco.delete()
    texto = request.user.username + " removeu o tronco: " +nome
    log = Log(log= texto)
    log.save()
    return redirect('/troncos/')

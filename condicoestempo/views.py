from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import CondicaoTempo, GrupoTempo
import re
from django_tables2 import RequestConfig
from .tables import CondicaoTempoTable
from anuncios.models import Anuncio , Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo
from troncos.models import Tronco
from logs.models import Log

@login_required
def add(request):
    dest_anuncios = Anuncio.objects.all()
    dest_gravacoes = Gravacao.objects.all()
    dest_numeros = NumeroEntrada.objects.all()
    dest_uras = URA.objects.all()
    dest_filas = Fila.objects.all()
    dest_chamadasGrupo = ChamadaEmGrupo.objects.all()
    dest_condicoes = CondicaoTempo.objects.all()
    dest_troncos = Tronco.objects.all()
    gravacoes = Gravacao.objects.exclude(musica__isnull=False)
    data = {}
    data['dest_anuncios'] = dest_anuncios
    data['dest_gravacoes'] = dest_gravacoes
    data['dest_numeros'] = dest_numeros
    data['dest_uras'] = dest_uras
    data['dest_filas'] = dest_filas
    data['dest_chamadasGrupo'] = dest_chamadasGrupo
    data['dest_condicoes'] = dest_condicoes
    data['dest_troncos'] = dest_troncos
    data['gravacoes'] = gravacoes
    return render(request, 'CadastroCondicoesTempo.html', data)

@login_required
def list(request):
    table = CondicaoTempoTable(CondicaoTempo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'condicoesTempo.html',{'table': table})

@login_required
def condicoestempo_novo(request):
    nome = request.POST['nome']

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

    condicoestempo = CondicaoTempo(nome=nome)
    condicoestempo.save()

    if destinoId != 0:
        condicoestempo.destinoCoincideTipo = tipoDestino
        condicoestempo.destinoCoincide = destinoId
        condicoestempo.save()

    if destinoId != 0:
        condicoestempo.destinoNaoCoincideTipo = ntipoDestino
        condicoestempo.destinoNaoCoincide = ndestinoId
        condicoestempo.save()

    tipo = '7'
    horaInicio = []
    horaFim = []
    diaSemanaInicio = []
    diaSemanaFim = []
    diaMesInicio = []
    diaMesFim = []
    mesIncio = []
    mesFim = []

    contador = int(request.POST['count'])
    for i in range(contador):
        horaInicio.append(request.POST['hora_inicio'+str(i)])
        horaFim.append(request.POST['hora_termino'+str(i)])
        diaSemanaInicio.append(request.POST['dia_semana_ini'+str(i)])
        diaSemanaFim.append(request.POST['dia_semana_ter'+str(i)])
        diaMesInicio.append(request.POST['dia_mes_inicio'+str(i)])
        diaMesFim.append(request.POST['dia_mes_termina'+str(i)])
        mesIncio.append(request.POST['mes_inicio'+str(i)])
        mesFim.append(request.POST['mes_termino'+str(i)])
    cont=0;
    while cont < contador:
        grupotempo = GrupoTempo( horaInicio=horaInicio[cont],horaFim=horaFim[cont], diaSemanaInicio=diaSemanaInicio[cont], tipo=tipo,
        diaSemanaFim=diaSemanaFim[cont], diaMesInicio=diaMesInicio[cont], diaMesFim= diaMesFim[cont],mesIncio=mesIncio[cont],mesFim=mesFim[cont], condTempo=condicoestempo)
        grupotempo.save()
        cont= cont + 1

    texto = request.user.username + " adicionou a condição de tempo: " +nome
    log = Log(log= texto)
    log.save()

    return redirect ('/condicoestempo/')

@login_required
def condicoestempo_edita(request, id):
    data = {}
    condicoestempo = CondicaoTempo.objects.get(id=id)
    data['condicoestempo'] = condicoestempo
    grupotempo = GrupoTempo.objects.get(condTempo=condicoestempo)
    data['grupotempo'] = grupotempo

    if request.method == 'POST':

        nome = request.POST['nome']
        condicoestempo.nome = nome
        condicoestempo.save()

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

        if destinoId != 0:
            condicoestempo.destinoCoincideTipo = tipoDestino
            condicoestempo.destinoCoincide = destinoId
            condicoestempo.save()

        if destinoId != 0:
            condicoestempo.destinoNaoCoincideTipo = ntipoDestino
            condicoestempo.destinoNaoCoincide = ndestinoId
            condicoestempo.save()

        horaInicio = request.POST['hora_inicio']
        horaFim = request.POST['hora_termino']
        diaSemanaInicio = request.POST['dia_semana_ini']
        diaSemanaFim = request.POST['dia_semana_ter']
        diaMesInicio = request.POST['dia_mes_inicio']
        diaMesFim = request.POST['dia_mes_termina']
        mesIncio = request.POST['mes_inicio']
        mesFim = request.POST['mes_termino']

        grupotempo.nome= nome
        grupotempo.horaInicio = horaInicio
        grupotempo.horaFim = horaFim
        grupotempo.diaSemanaInicio = diaSemanaInicio
        grupotempo.diaSemanaFim = diaSemanaFim
        grupotempo.diaMesInicio = diaMesInicio
        grupotempo.diaMesFim = diaMesFim
        grupotempo.mesIncio = mesIncio
        grupotempo.mesFim = mesFim

        grupotempo.save()
        texto = request.user.username + " editou a condição de tempo: " +nome
        log = Log(log= texto)
        log.save()

        return redirect('/condicoestempo/')
    else:
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
        return render(request, 'editaCondicaoTempo.html', data)


@login_required
def condicoestempo_remove(request, id):
    condicoestempo = CondicaoTempo.objects.get(id=id)
    nome = condicoestempo.nome
    condicoestempo.delete()
    texto = request.user.username + " removeu a condição de tempo: " +nome
    log = Log(log= texto)
    log.save()
    return redirect('/condicoestempo/')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FilaForm
from .models import Fila
import re
from django_tables2 import RequestConfig
from .tables import FilaTable
from musicas.models import Musica
from numeros.models import NumeroEntrada
from destinos.models import Destino
from uras.models import URA
from anuncios.models import Anuncio, Gravacao
from numeros.models import NumeroEntrada
from uras.models import URA
from filas.models import Fila
from chamadasgrupo.models import ChamadaEmGrupo
from condicoestempo.models import CondicaoTempo
from troncos.models import Tronco
from django.shortcuts import render, redirect
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
    anun_conf_chamada = Anuncio.objects.all()
    musicas = Musica.objects.all()
    anun_uniao = Anuncio.objects.all()
    agen_anunc = Anuncio.objects.all()
    break_out = URA.objects.all()
    data['dest_anuncios'] = dest_anuncios
    data['dest_gravacoes'] = dest_gravacoes
    data['dest_numeros'] = dest_numeros
    data['dest_uras'] = dest_uras
    data['dest_filas'] = dest_filas
    data['dest_chamadasGrupo'] = dest_chamadasGrupo
    data['dest_condicoes'] = dest_condicoes
    data['dest_troncos'] = dest_troncos
    data['anun_conf_chamada'] = anun_conf_chamada
    data['musicas'] = musicas
    data['anun_uniao'] = anun_uniao
    data['agen_anunc'] = agen_anunc
    data['break_out'] = break_out
    return render(request, 'CadastroFila.html', data)

@login_required
def list(request):
    table = FilaTable(Fila.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'filas.html',{'table': table})

@login_required
def fila_novo(request):
    nome = request.POST['nome']
    senha = request.POST['senha']
    if 'dicas_disp' in request.POST:
        dicasDisp = request.POST['dicas_disp']
    else:
        dicasDisp = False
    if 'conf_cham' in request.POST:
        confirmCham = request.POST['conf_cham']
    else:
        confirmCham = False
    anuncConfirmCham = request.POST['anunc_confirm_cham']
    if anuncConfirmCham != '0':
        anuncConfirmCham = Anuncio.objects.get(id=anuncConfirmCham)
    prefixCID = request.POST['prefix_cid']
    prefixTempoEspera = request.POST['prefix_tempo']
    infoAlerta = request.POST['info']
    restringAgentDin = request.POST['restring_agent_din']
    restricAgente = request.POST['restric_agente']

    estratChamada = request.POST['estrat_ring']
    if 'p_auto' in request.POST:
        preenchAuto = request.POST['p_auto']
    else:
        preenchAuto = False
    igAgentesOcup = request.POST['ignorar_agen_ocup']
    pesoFila = request.POST['peso']
    musEspera = request.POST['musica_esp']
    if musEspera != '0':
        musEspera = Musica.objects.get(id=musEspera)
    tipoMus = request.POST['tipo_mus']
    anuncUniao = request.POST['anuncio_uniao']
    if anuncUniao !='0':
        anuncUniao = Anuncio.objects.get(id=anuncUniao)
    quandoAnun = request.POST['quando_anuncio']
    gravacaoChamada = request.POST['grav_cham']
    modoGravacao = request.POST['modo_grav']
    ajustVolumeChamada = request.POST['vol_cham']
    ajustVolumeAgente = request.POST['vol_agent']
    if 'mcrol' in request.POST:
        marcaChamOutroLug = request.POST['mcrol']
    else:
        marcaChamOutroLug = False

    maxTempoEspera = request.POST['max_temp']
    modoMaxTempoEspera = request.POST['modo_max_esp']
    tempoLimAgent = request.POST['limit_temp_agente']
    reinicioTempoLimAg = request.POST['rest_agnt']
    retentativa = request.POST['retentativa']
    tempoConclusao = request.POST['temp_conclu']
    atrasoMembro = request.POST['atraso_membro']
    anuncioAgente = request.POST['agnt_a']
    if anuncioAgente != '0':
        anuncioAgente = Anuncio.objects.get(id=anuncioAgente)
    relatorioTemEsp = request.POST['report_time']
    pausaAutom = request.POST['pausa_auto']
    pausaAutoOcup = request.POST['pausa_ocup']
    pausaAutoIndispo = request.POST['pausa_ind']
    atrasoPausaAut = request.POST['delay_pausa']

    maxChamadores = request.POST['max_callers']
    unirVazio = request.POST['join_empty']
    deixarVazio = request.POST['leave_empty']
    limMembrosPenal = request.POST['penalty']

    frequencia = request.POST['frequency']
    posAnuncio = request.POST['position_anun']
    anuncTempoEsp = request.POST['anun_tempEsp']

    menuSaidaURA = request.POST['break_out']
    if menuSaidaURA != '0':
        menuSaidaURA = URA.objects.get(id=menuSaidaURA)
    frequenRepet = request.POST['r_frequency']

    eventChamado = request.POST['event_called']
    eventStatusMem = request.POST['event_status']
    nivelServico = request.POST['service_level']
    filtro = request.POST['filtro_regex']

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

    destinoId = '0'
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

    reporEstat = request.POST['repor_estat']

    tipo = '5'

    fila = Fila(nome=nome,
                senha=senha,
                dicasDisp=dicasDisp,
                confirmCham=confirmCham,
                prefixCID=prefixCID,
                prefixTempoEspera=prefixTempoEspera,
                infoAlerta=infoAlerta,
                restringAgentDin=restringAgentDin,
                restricAgente=restricAgente,
                estratChamada=estratChamada,
                preenchAuto=preenchAuto,
                igAgentesOcup = igAgentesOcup,
                pesoFila = pesoFila,
                tipoMus = tipoMus,
                quandoAnun = quandoAnun,
                gravacaoChamada = gravacaoChamada,
                modoGravacao = modoGravacao,
                ajustVolumeChamada = ajustVolumeChamada,
                ajustVolumeAgente = ajustVolumeAgente,
                marcaChamOutroLug=marcaChamOutroLug,
                maxTempoEspera = maxTempoEspera,
                modoMaxTempoEspera = modoMaxTempoEspera,
                tempoLimAgent = tempoLimAgent,
                reinicioTempoLimAg = reinicioTempoLimAg,
                retentativa = retentativa,
                tempoConclusao = tempoConclusao,
                atrasoMembro = atrasoMembro,
                relatorioTemEsp = relatorioTemEsp,
                pausaAutom = pausaAutom,
                pausaAutoOcup = pausaAutoOcup,
                pausaAutoIndispo = pausaAutoIndispo,
                atrasoPausaAut = atrasoPausaAut,
                maxChamadores = maxChamadores,
                unirVazio = unirVazio,
                deixarVazio = deixarVazio,
                frequencia = frequencia,
                posAnuncio = posAnuncio,
                anuncTempoEsp = anuncTempoEsp,
                frequenRepet = frequenRepet,
                eventChamado = eventChamado,
                eventStatusMem = eventStatusMem,
                nivelServico = nivelServico,
                filtro = filtro,
                reporEstat = reporEstat,
                tipo=tipo
                )
    fila.save()

    if destinoId != '0':
        fila.destinoFalhaTipo = tipoDestino
        fila.destinoFalha = destinoId
        fila.save()

    if anuncConfirmCham != '0':
        fila.anuncConfirmCham=anuncConfirmCham
        fila.save()

    if musEspera != '0':
        fila.musEspera = musEspera
        fila.save()

    if anuncUniao !='0':
        fila.anuncUniao = anuncUniao
        fila.save()

    if anuncioAgente != '0':
        fila.anuncioAgente = anuncioAgente
        fila.save()

    if menuSaidaURA != '0':
        fila.menuSaidaURA = menuSaidaURA
        fila.save()

    if limMembrosPenal !='0':
        fila.limMembrosPenal = limMembrosPenal

    texto = request.user.username + " adicionou a fila: " +nome
    log = Log(log= texto)
    log.save()

    return redirect ('/filas/')

@login_required
def fila_edita(request, id):
    data = {}

    fila = Fila.objects.get(id=id)
    data['fila'] = fila
    if request.method == 'POST':
        nome = request.POST['nome']
        senha = request.POST['senha']
        if 'dicas_disp' in request.POST:
            dicasDisp = request.POST['dicas_disp']
        else:
            dicasDisp = False
        if 'conf_cham' in request.POST:
            confirmCham = request.POST['conf_cham']
        else:
            confirmCham = False
        anuncConfirmCham = request.POST['anunc_confirm_cham']
        if anuncConfirmCham != '0':
            anuncConfirmCham = Anuncio.objects.get(id=anuncConfirmCham)
        prefixCID = request.POST['prefix_cid']
        prefixTempoEspera = request.POST['prefix_tempo']
        infoAlerta = request.POST['info']
        restringAgentDin = request.POST['restring_agent_din']
        restricAgente = request.POST['restric_agente']

        estratChamada = request.POST['estrat_ring']
        if 'p_auto' in request.POST:
            preenchAuto = request.POST['p_auto']
        else:
            preenchAuto = False
        igAgentesOcup = request.POST['ignorar_agen_ocup']
        pesoFila = request.POST['peso']
        musEspera = request.POST['musica_esp']
        if musEspera != '0':
            musEspera = Musica.objects.get(id=musEspera)
        tipoMus = request.POST['tipo_mus']
        anuncUniao = request.POST['anuncio_uniao']
        if anuncUniao !='0':
            anuncUniao = Anuncio.objects.get(id=anuncUniao)
        quandoAnun = request.POST['quando_anuncio']
        gravacaoChamada = request.POST['grav_cham']
        modoGravacao = request.POST['modo_grav']
        ajustVolumeChamada = request.POST['vol_cham']
        ajustVolumeAgente = request.POST['vol_agent']
        if 'mcrol' in request.POST:
            marcaChamOutroLug = request.POST['mcrol']
        else:
            marcaChamOutroLug = False

        maxTempoEspera = request.POST['max_temp']
        modoMaxTempoEspera = request.POST['modo_max_esp']
        tempoLimAgent = request.POST['limit_temp_agente']
        reinicioTempoLimAg = request.POST['rest_agnt']
        retentativa = request.POST['retentativa']
        tempoConclusao = request.POST['temp_conclu']
        atrasoMembro = request.POST['atraso_membro']
        anuncioAgente = request.POST['agnt_a']
        if anuncioAgente != '0':
            anuncioAgente = Anuncio.objects.get(id=anuncioAgente)
        relatorioTemEsp = request.POST['report_time']
        pausaAutom = request.POST['pausa_auto']
        pausaAutoOcup = request.POST['pausa_ocup']
        pausaAutoIndispo = request.POST['pausa_ind']
        atrasoPausaAut = request.POST['delay_pausa']

        maxChamadores = request.POST['max_callers']
        unirVazio = request.POST['join_empty']
        deixarVazio = request.POST['leave_empty']
        limMembrosPenal = request.POST['penalty']

        frequencia = request.POST['frequency']
        posAnuncio = request.POST['position_anun']
        anuncTempoEsp = request.POST['anun_tempEsp']

        menuSaidaURA = request.POST['break_out']
        if menuSaidaURA != '0':
            menuSaidaURA = URA.objects.get(id=menuSaidaURA)
        frequenRepet = request.POST['r_frequency']

        eventChamado = request.POST['event_called']
        eventStatusMem = request.POST['event_status']
        nivelServico = request.POST['service_level']
        filtro = request.POST['filtro_regex']

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

        destinoId = '0'
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

        reporEstat = request.POST['repor_estat']

        fila.nome=nome
        fila.senha=senha
        fila.dicasDisp=dicasDisp
        fila.confirmCham=confirmCham
        fila.prefixCID=prefixCID
        fila.prefixTempoEspera=prefixTempoEspera
        fila.infoAlerta=infoAlerta
        fila.restringAgentDin=restringAgentDin
        fila.restricAgente=restricAgente
        fila.estratChamada=estratChamada
        fila.preenchAuto=preenchAuto
        fila.igAgentesOcup = igAgentesOcup
        fila.pesoFila = pesoFila
        fila.tipoMus = tipoMus
        fila.quandoAnun = quandoAnun
        fila.gravacaoChamada = gravacaoChamada
        fila.modoGravacao = modoGravacao
        fila.ajustVolumeChamada = ajustVolumeChamada
        fila.ajustVolumeAgente = ajustVolumeAgente
        fila.marcaChamOutroLug=marcaChamOutroLug
        fila.maxTempoEspera = maxTempoEspera
        fila.modoMaxTempoEspera = modoMaxTempoEspera
        fila.tempoLimAgent = tempoLimAgent
        fila.reinicioTempoLimAg = reinicioTempoLimAg
        fila.retentativa = retentativa
        fila.tempoConclusao = tempoConclusao
        fila.atrasoMembro = atrasoMembro
        fila.relatorioTemEsp = relatorioTemEsp
        fila.pausaAutom = pausaAutom
        fila.pausaAutoOcup = pausaAutoOcup
        fila.pausaAutoIndispo = pausaAutoIndispo
        fila.atrasoPausaAut = atrasoPausaAut
        fila.maxChamadores = maxChamadores
        fila.unirVazio = unirVazio
        fila.deixarVazio = deixarVazio
        fila.frequencia = frequencia
        fila.posAnuncio = posAnuncio
        fila.anuncTempoEsp = anuncTempoEsp
        fila.frequenRepet = frequenRepet
        fila.eventChamado = eventChamado
        fila.eventStatusMem = eventStatusMem
        fila.nivelServico = nivelServico
        fila.filtro = filtro
        fila.reporEstat = reporEstat
        fila.save()

        if limMembrosPenal != '0':
            fila.limMembrosPenal = limMembrosPenal
            fila.save()

        if destinoId != '0':
            fila.destinoFalhaTipo = tipoDestino
            fila.destinoFalha = destinoId
            fila.save()

        if anuncConfirmCham != '0':
            fila.anuncConfirmCham=anuncConfirmCham
            fila.save()

        if musEspera != '0':
            fila.musEspera = musEspera
            fila.save()

        if anuncUniao !='0':
            fila.anuncUniao = anuncUniao
            fila.save()

        if anuncioAgente != '0':
            fila.anuncioAgente = anuncioAgente
            fila.save()

        if menuSaidaURA != '0':
            fila.menuSaidaURA = menuSaidaURA
            fila.save()
        texto = request.user.username + " editou a fila: " +fila.nome
        log = Log(log= texto)
        log.save()

        return redirect('/filas/')
    else:
        dest_anuncios = Anuncio.objects.all()
        dest_gravacoes = Gravacao.objects.all()
        dest_numeros = NumeroEntrada.objects.all()
        dest_uras = URA.objects.all()
        dest_filas = Fila.objects.all()
        dest_chamadasGrupo = ChamadaEmGrupo.objects.all()
        dest_condicoes = CondicaoTempo.objects.all()
        dest_troncos = Tronco.objects.all()
        anun_conf_chamada = Anuncio.objects.all()
        musicas = Musica.objects.all()
        anun_uniao = Anuncio.objects.all()
        agen_anunc = Anuncio.objects.all()
        break_out = URA.objects.all()
        data['dest_anuncios'] = dest_anuncios
        data['dest_gravacoes'] = dest_gravacoes
        data['dest_numeros'] = dest_numeros
        data['dest_uras'] = dest_uras
        data['dest_filas'] = dest_filas
        data['dest_chamadasGrupo'] = dest_chamadasGrupo
        data['dest_condicoes'] = dest_condicoes
        data['dest_troncos'] = dest_troncos
        data['anun_conf_chamada'] = anun_conf_chamada
        data['musicas'] = musicas
        data['anun_uniao'] = anun_uniao
        data['agen_anunc'] = agen_anunc
        data['break_out'] = break_out

        return render(request, 'editaFila.html', data)

@login_required
def fila_remove(request, id):
    fila = Fila.objects.get(id=id)
    nome = fila.nome
    fila.delete()
    texto = request.user.username + " removeu a fila: " +nome
    log = Log(log= texto)
    log.save()

    return redirect('/filas/')

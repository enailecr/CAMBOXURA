from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FilaForm
from .models import Fila
import re
from django_tables2 import RequestConfig
from .tables import FilaTable


@login_required
def add(request):
    form = FilaForm()
    data = {'form' : form}
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
    tipoMus = request.POST['tipo_mus']
    anuncUniao = request.POST['anuncio_uniao']
    quandoAnun = request.POST['quando_anuncio']
    gravacaoChamada = request.POST['grav_cham']
    modoGravacao = request.POST['modo_grav']
    ajustVolumeChamada = request.POST['vol_cham']
    ajustVolumeAgente = request.POST['vol_agent']
    if 'mcrol' in request.POST:
        marcaChamOutroLug = request.POST['mcrol']
    else:
        marcaChamOutroLug = False

    maxTempoEspera = request.POST['mcrol']
    modoMaxTempoEspera = request.POST['modo_max_esp']
    tempoLimAgent = request.POST['limit_temp_agente']
    reinicioTempoLimAg = request.POST['rest_agnt']
    retentativa = request.POST['retentativa']
    tempoConclusao = request.POST['temp_conclu']
    atrasoMembro = request.POST['atraso_membro']
    anuncioAgente = request.POST['agnt_a']
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
    frequenRepet = request.POST['r_frequency']

    eventChamado = request.POST['event_called']
    eventStatusMem = request.POST['event_status']
    nivelServico = request.POST['service_level']
    filtro = request.POST['filtro_regex']

    destinoFalha = request.POST['dest_falha']

    reporEstat = request.POST['repor_estat']

    tipo = '5'

    fila = Fila(nome=nome,
                senha=senha,
                dicasDisp=dicasDisp,
                confirmCham=confirmCham,
                anuncConfirmCham=anuncConfirmCham,
                prefixCID=prefixCID,
                prefixTempoEspera=prefixTempoEspera,
                infoAlerta=infoAlerta,
                restringAgentDin=restringAgentDin,
                restricAgente=restricAgente,
                estratChamada=estratChamada,
                preenchAuto=preenchAuto,
                igAgentesOcup = igAgentesOcup,
                pesoFila = pesoFila,
                musEspera = musEspera,
                tipoMus = tipoMus,
                anuncUniao = anuncUniao,
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
                anuncioAgente = anuncioAgente,
                relatorioTemEsp = relatorioTemEsp,
                pausaAutom = pausaAutom,
                pausaAutoOcup = pausaAutoOcup,
                pausaAutoIndispo = pausaAutoIndispo,
                atrasoPausaAut = atrasoPausaAut,
                maxChamadores = maxChamadores,
                unirVazio = unirVazio,
                deixarVazio = deixarVazio,
                limMembrosPenal = limMembrosPenal,
                frequencia = frequencia,
                posAnuncio = posAnuncio,
                anuncTempoEsp = anuncTempoEsp,
                menuSaidaURA = menuSaidaURA,
                frequenRepet = frequenRepet,
                eventChamado = eventChamado,
                eventStatusMem = eventStatusMem,
                nivelServico = nivelServico,
                filtro = filtro,
                destinoFalha = destinoFalha,
                reporEstat = reporEstat,
                tipo=tipo
                )
    fila.save()

    return redirect ('/filas/')

@login_required
def fila_edita(request):
        return redirect('/filas/')
    else:
        return render(request, 'editafila.html')

@login_required
def fila_remove(request, id):
    fila = Fila.objects.get(id=id)
    fila.delete()
    return redirect('/filas/')
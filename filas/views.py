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

    return redirect ('/filas/')

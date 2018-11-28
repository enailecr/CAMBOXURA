from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import re
from django_tables2 import RequestConfig
from .forms import LogsForm
from .tables import LogsTable, LogsCamboxTable
from .models import Log, LogCambox
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import pytz

@login_required
def list(request):

    table = LogsTable(Log.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logs.html',{'table': table})

@login_required
def busca_logs(request):
    utc=pytz.UTC

    tipoLog = request.POST['tipo_log']
    di = request.POST['data_inicio']
    df = request.POST['data_fim']

    dataInicio = None
    dataFim = None
    if di:
        dataInicio = datetime.strptime(di, '%Y-%m-%d')
        dataInicio = utc.localize(dataInicio)
    if df:
        dataFim = datetime.strptime(df, '%Y-%m-%d')
        dataFim = utc.localize(dataFim)

    logs = []
    if tipoLog == "ura":
        try:
            logs = Log.objects.filter(log__icontains='URA')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "num":
        try:
            logs = Log.objects.filter(log__icontains='número')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "tronco":
        try:
            logs = Log.objects.filter(log__icontains='tronco')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "anun":
        try:
            logs = Log.objects.filter(log__icontains='anúncio')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "cham":
        try:
            logs = Log.objects.filter(log__icontains='chamada em grupo')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "fila":
        try:
            logs = Log.objects.filter(log__icontains='fila:')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "mus":
        try:
            logs = Log.objects.filter(log__icontains='música')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "cond":
        try:
            logs = Log.objects.filter(log__icontains='condição')
        except ObjectDoesNotExist:
            pass
    if tipoLog == "todos":
        logs = Log.objects.all()

    logs_filtrados = []
    if logs:
        if dataInicio or dataFim:
            for log in logs:
                if dataInicio:
                    if dataInicio< log.data:
                        if dataFim:
                            if dataFim >log.data:
                                logs_filtrados.append(log)
                        else:
                            logs_filtrados.append(log)
                else:
                    if dataFim >log.data:
                        logs_filtrados.append(log)
        else:
            logs_filtrados = logs

    data = {}
    data['dataInicio'] = di
    data['dataFim'] = df
    data['tipoLog'] = tipoLog
    table = LogsTable(logs_filtrados)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logs.html',data)

@login_required
def lista_logs_cambox(request):

    arq = open('/var/log/asterisk/cambox', 'r')
    texto = arq.readlines()
    logs = []

    for linha in texto :
        grupo = re.match('(\[)(....-..-.. ..:..:..)(\] )(.*)(\[)(.*)(\]\[)(.{10})(\])(.*)', linha)
        data = grupo.group(2)
        tipoLog = grupo.group(4)
        processo = grupo.group(6)
        chamada = grupo.group(8)
        log = grupo.group(10)
        log = LogCambox(data=data,tipo=tipoLog, processo=processo,chamada=chamada,log=log)
        logs.append(log)
    arq.close()

    data = {}
    table = LogsCamboxTable(logs)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logsCambox.html',data)

@login_required
def busca_logs_cambox(request):

    dataInicio = request.POST['data_inicio']
    dataFim = request.POST['data_fim']
    chamada = request.POST['chamada']
    processo = request.POST['processo']
    tipoLog = request.POST['tipo_log']

    arq = open('/var/log/asterisk/cambox', 'r')
    texto = arq.readlines()
    logs = []

    if chamada:
        if processo:
            padrao = '(\[)(....-..-.. ..:..:..)(\] )(.*)(\[)('+processo+')(\]\[)('+chamada+')(\])(.*)'
            if tipoLog:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )('+tipoLog+')(\[)('+processo+')(\]\[)('+chamada+')(\])(.*)'
        else:
            if tipoLog:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )('+tipoLog+')(\[)(.*)(\]\[)('+chamada+')(\])(.*)'
            else:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )(.*)(\[)(.*)(\]\[)('+chamada+')(\])(.*)'
    else:
        if processo:
            padrao = '(\[)(....-..-.. ..:..:..)(\] )(.*)(\[)('+processo+')(\]\[)(.{10})(\])(.*)'
            if tipoLog:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )('+tipoLog+')(\[)('+processo+')(\]\[)(.{10})(\])(.*)'
        else:
            if tipoLog:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )('+tipoLog+')(\[)(.*)(\]\[)(.{10})(\])(.*)'
            else:
                padrao = '(\[)(....-..-.. ..:..:..)(\] )(.*)(\[)(.*)(\]\[)(.{10})(\])(.*)'

    for linha in texto :
        grupo = re.match(padrao, linha)
        if grupo:
            dat = grupo.group(2)
            tipoLo = grupo.group(4)
            process = grupo.group(6)
            chamad = grupo.group(8)
            lo = grupo.group(10)
            log = LogCambox(data=dat,tipo=tipoLo, processo=process,chamada=chamad,log=lo)
            logs.append(log)
    arq.close()

    logs_filtrados = []
    if logs:
        if dataInicio or dataFim:
            for log in logs:
                if dataInicio:
                    if dataInicio< log.data:
                        if dataFim:
                            if dataFim >log.data:
                                logs_filtrados.append(log)
                        else:
                            logs_filtrados.append(log)
                else:
                    if dataFim >log.data:
                        logs_filtrados.append(log)
        else:
            logs_filtrados = logs

    data = {}
    table = LogsCamboxTable(logs_filtrados)
    data['dataInicio'] = dataInicio
    data['dataFim'] = dataFim
    data['tipoLog'] = tipoLog
    data['chamada'] = chamada
    data['processo'] = processo
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logsCambox.html',data)

@login_required
def lista_logs_server(request):
    data = {}
    data['dataInicio'] = di
    data['dataFim'] = df
    data['tipoLog'] = tipoLog
    table = LogsTable(logs_filtrados)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logs.html',data)

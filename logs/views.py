from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import re
from django_tables2 import RequestConfig
from .forms import LogsForm
from .tables import LogsTable
from .models import Log
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
#PROCESO E CHAMADA
    data = {}
    data['dataInicio'] = di
    data['dataFim'] = df
    data['tipoLog'] = tipoLog
    table = LogsTable(logs_filtrados)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logs.html',data)

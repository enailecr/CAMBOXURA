from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import  Cdr, Canal, Regex
import re
from django_tables2 import RequestConfig
from .tables import RelatoriosTable, CanaisTable
from datetime import datetime
import pytz

@login_required
def list(request):
    relatorios = Cdr.objects.using('relatorios').all()
    table = RelatoriosTable(relatorios)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'relatorios.html',{'table': table})

@login_required
def lista_canais(request):
    relatorios = Canal.objects.using('relatorios').all()
    table = CanaisTable(relatorios)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'canais.html',{'table': table})

@login_required
def busca_relatorios(request):
    utc=pytz.UTC

    if 'campo' in request.POST:
        campo = request.POST['campo']
        request.session['campo'] = request.POST['campo']
    else:
        campo = request.session['campo']
    if 'campo_input' in request.POST:
        campo_input = request.POST['campo_input']
        request.session['campo_input'] = request.POST['campo_input']
    else:
        campo_input = request.session['campo_input']
    if 'status' in request.POST:
        status = request.POST['status']
        request.session['status'] = request.POST['status']
    else:
        status = request.session['status']
    if 'data_inicio' in request.POST:
        di = request.POST['data_inicio']
        request.session['dataInicioRelatorio'] = request.POST['data_inicio']
    else:
        di = request.session['dataInicioRelatorio']
    if 'data_fim' in request.POST:
        df = request.POST['data_fim']
        request.session['dataFimRelatorio'] = request.POST['data_fim']
    else:
        df = request.session['dataFimRelatorio']

    dataInicio = None
    dataFim = None
    if di:
        dataInicio = datetime.strptime(di, '%Y-%m-%d')
        dataInicio = utc.localize(dataInicio)
    if df:
        dataFim = datetime.strptime(df, '%Y-%m-%d')
        dataFim = utc.localize(dataFim)

    if dataInicio or dataFim:
        if dataInicio:
            if dataFim:
                relatorios = Cdr.objects.using('relatorios').filter(calldate__range=[dataInicio, dataFim])
            else:
                relatorios = Cdr.objects.using('relatorios').filter(calldate__gte=dataInicio)
        else:
            relatorios = Cdr.objects.using('relatorios').exclude(calldate__gte=dataFim)
    else:
        relatorios =  Cdr.objects.using('relatorios').all()

    if status:
        relatorios = relatorios.filter(disposition=status)

    if campo == "org":
        relatorios = relatorios.filter(src=campo_input)

    if campo == "dest":
        relatorios = relatorios.filter(dst=campo_input)

    data = {}
    data['dataInicioRelatorio'] = di
    data['dataFimRelatorio'] = df
    data['campo'] = campo
    data['campo_input'] = campo_input
    data['status'] = status
    table = RelatoriosTable(relatorios)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'relatorios.html',data)

@login_required
def canal_novo(request):
    return render(request, 'regex_canal.html')

@login_required
def add_canal(request):
    nome = request.POST['nome']
    canal = Canal(nome=nome)
    canal.save(using='relatorios')

    regras = []

    contador = int(request.POST['count'])
    for i in range(contador):
        regras.append(request.POST['regex'+str(i)])

    cont=0;
    while cont < contador:
        regex = Regex(expressao = regras[cont], canal=canal)
        regex.save(using='relatorios')
        cont= cont + 1

    return render(request, 'regex_canal.html')

@login_required
def canal_remove(request, id):
    canal = Canal.objects.using('relatorios').get(id=id)
    canal.delete()

    return redirect('/relatorios/canais/')

@login_required
def canal_edita(request, id):
    canal = Canal.objects.using('relatorios').get(id=id)
    data['canal'] = canal
    return render(request, 'edita_regex_canal.html',data)

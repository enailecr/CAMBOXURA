from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import  Cdr, Canal, Regex
import re
from django_tables2 import RequestConfig
from .tables import RelatoriosTable, CanaisTable
from datetime import datetime
import pytz
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.core.files.storage import FileSystemStorage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

@login_required
def list(request):
    relatorios = Cdr.objects.using('relatorios').all()
    regras = Regex.objects.using('relatorios').all()
    for registro in relatorios:
        if registro.disposition == "NO ANSWER":
            registro.disposition = "Sem resposta"
        if registro.disposition == "BUSY":
            registro.disposition = "Ocupado"
        if registro.disposition == "ANSWERED":
            registro.disposition = "Respondido"
        if registro.disposition == "FAILED":
            registro.disposition = "Falha"
        for regra in regras:
            string = "("+regra.expressao+")"+"(.*?)(-)(.*)"
            canalorigem = re.match(string, registro.channel)
            if canalorigem:
                canal = regra.canal.nome
                registro.channel = canal
            canaldest = re.match(string, registro.dstchannel)
            if canaldest:
                canal = regra.canal.nome
                registro.dstchannel = canal

    table = RelatoriosTable(relatorios)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    if export_format=="pdf":
        doc = SimpleDocTemplate("/tmp/relatorio.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
        doc.pagesize = landscape(A4)
        elements = []
        s = getSampleStyleSheet()

        data = [['Data','Origem','Destino','Canal Origem','Canal Destino','Duração','Status']]
        for registro in relatorios:
            linha = []
            linha.append(registro.calldate.strftime('%m/%d/%Y %H:%M:%S'))
            linha.append(str(registro.src))
            linha.append(str(registro.dst))
            linha.append(str(registro.channel))
            linha.append(str(registro.dstchannel))
            linha.append(str(registro.duration))
            linha.append(str(registro.disposition))
            data.append(linha)

        style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])

        s = s["BodyText"]
        s.wordWrap = 'CJK'
        # data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        t=Table(data)
        t.setStyle(style)

        #Send the data and build the file
        elements.append(t)
        doc.build(elements)

        fs = FileSystemStorage("/tmp")
        with fs.open("relatorio.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
            return response

        return response

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

    regras = Regex.objects.using('relatorios').all()
    for registro in relatorios:
        if registro.disposition == "NO ANSWER":
            registro.disposition = "Sem resposta"
        if registro.disposition == "BUSY":
            registro.disposition = "Ocupado"
        if registro.disposition == "ANSWERED":
            registro.disposition = "Respondido"
        if registro.disposition == "FAILED":
            registro.disposition = "Falha"
        for regra in regras:
            string = "("+regra.expressao+")"+"(.*?)(-)(.*)"
            canalorigem = re.match(string, registro.channel)
            if canalorigem:
                canal = regra.canal.nome
                registro.channel = canal
            canaldest = re.match(string, registro.dstchannel)
            if canaldest:
                canal = regra.canal.nome
                registro.dstchannel = canal

    rel_filtrado =[]
    if campo == "cano" or campo == "cand":
        for registro in relatorios:
            if ((campo == "cano" and re.match('(.*?)'+campo_input+'(.*?)', registro.channel)) or (campo == "cand" and re.match('(.*?)'+campo_input+'(.*?)', registro.dstchannel))):
                rel_filtrado.append(registro)

    if rel_filtrado:
        relatorios = rel_filtrado

    data = {}
    data['dataInicioRelatorio'] = di
    data['dataFimRelatorio'] = df
    data['campo'] = campo
    data['campo_input'] = campo_input
    data['status'] = status
    table = RelatoriosTable(relatorios)
    data['table'] = table
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    export_format = request.GET.get('_export', None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))

    if export_format=="pdf":
        doc = SimpleDocTemplate("/tmp/relatorio.pdf", pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
        doc.pagesize = landscape(A4)
        elements = []
        s = getSampleStyleSheet()

        data = [['Data','Origem','Destino','Canal Origem','Canal Destino','Duração','Status']]
        for registro in relatorios:
            linha = []
            linha.append(registro.calldate.strftime('%m/%d/%Y %H:%M:%S'))
            linha.append(str(registro.src))
            linha.append(str(registro.dst))
            linha.append(str(registro.channel))
            linha.append(str(registro.dstchannel))
            linha.append(str(registro.duration))
            linha.append(str(registro.disposition))
            data.append(linha)

        style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                       ('VALIGN',(0,0),(0,-1),'TOP'),
                       ('ALIGN',(0,-1),(-1,-1),'CENTER'),
                       ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ])

        s = s["BodyText"]
        s.wordWrap = 'CJK'
        # data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        t=Table(data)
        t.setStyle(style)

        #Send the data and build the file
        elements.append(t)
        doc.build(elements)

        fs = FileSystemStorage("/tmp")
        with fs.open("relatorio.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
            return response

        return response

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
    data = {}
    canal = Canal.objects.using('relatorios').get(id=id)
    data['canal'] = canal
    regras = Regex.objects.using('relatorios').filter(canal=canal)
    data['regras'] = regras
    count= len(regras)
    data['count'] = count
    if request.method == 'POST':
        nome = request.POST['nome']
        canal.nome = nome
        canal.save(using='relatorios')

        cont=0;
        for r in regras:
            r.delete()

        regra =[]
        contador = int(request.POST['count'])
        conta= 0
        for i in range(contador):
            if 'regex'+str(i) in request.POST:
                regra.append(request.POST['regex'+str(i)])
                conta = conta +1

        while cont < conta:
            regex = Regex(expressao = regra[cont], canal=canal)
            regex.save(using='relatorios')
            cont= cont + 1

        return redirect('/relatorios/canais/')
    else:
        return render(request, 'edita_regex_canal.html',data)

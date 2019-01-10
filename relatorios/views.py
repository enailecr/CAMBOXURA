from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import  Cdr, Canal, Regex, Variaveis
import re
from django_tables2 import RequestConfig
from .tables import RelatoriosTable, CanaisTable
import time
from datetime import datetime, date
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
from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.db import connections
from datetime import timedelta
from django.db.models import Count

@login_required
def list(request):
    mesAtras = date.today() - timedelta(days=30)
    relatorios = Cdr.objects.using('relatorios').filter(calldate__gte=mesAtras)
    regras = Regex.objects.using('relatorios').all()
    variaveis = Variaveis.objects.using('relatorios').values('variavel').annotate(dcount=Count('variavel'))

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
        html_string = render_to_string('pdf.html', {'relatorios': relatorios})
        html = HTML(string=html_string)
        result = html.write_pdf()

        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename=list_people.pdf'
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'r')
            response.write(output.read())

        return response
    data = {}
    data['table'] = table
    data['variaveis'] = variaveis
    mesAtras = mesAtras.strftime('%Y-%m-%d')
    print(mesAtras)
    data['dataInicioRelatorio'] = mesAtras

    return render(request, 'relatorios.html',data)

@login_required
def detalhes(request):
    id = request.GET.get('id', None)
    chamada = Cdr.objects.using('relatorios').get(uniqueid=id)
    variaveis = Variaveis.objects.using('relatorios').filter(uniqueid=id)
    regras = Regex.objects.using('relatorios').all()

    detalhes = {}
    detalhes['calldate'] = chamada.calldate.strftime('%d/%m/%Y %H:%M:%S')
    detalhes['clid'] = chamada.clid
    detalhes['src'] = chamada.src
    detalhes['dst'] = chamada.dst
    detalhes['dcontext'] = chamada.dcontext
    for regra in regras:
        string = "("+regra.expressao+")"+"(.*?)(-)(.*)"
        canalorigem = re.match(string, chamada.channel)
        if canalorigem:
            canal = regra.canal.nome
            chamada.channel = canal
        canaldest = re.match(string, chamada.dstchannel)
        if canaldest:
            canal = regra.canal.nome
            chamada.dstchannel = canal

    detalhes['channel'] = chamada.channel
    detalhes['dstchannel'] = chamada.dstchannel
    detalhes['lastapp'] = chamada.lastapp
    detalhes['lastdata'] = chamada.lastdata
    detalhes['duration'] = chamada.duration
    detalhes['billsec'] = chamada.billsec
    if chamada.disposition == "NO ANSWER":
        chamada.disposition = "Sem resposta"
    if chamada.disposition == "BUSY":
        chamada.disposition = "Ocupado"
    if chamada.disposition == "ANSWERED":
        chamada.disposition = "Respondido"
    if chamada.disposition == "FAILED":
        chamada.disposition = "Falha"
    detalhes['disposition'] = chamada.disposition
    detalhes['amaflags'] = chamada.amaflags
    detalhes['accountcode'] = chamada.accountcode
    detalhes['userfield'] = chamada.userfield
    if chamada.recordingfile:
        detalhes['recordingfile'] = chamada.recordingfile.url
    detalhes['cnum'] = chamada.cnum
    detalhes['cnam'] = chamada.cnam
    detalhes['outbound_cnum'] = chamada.outbound_cnum
    detalhes['outbound_cnam'] = chamada.outbound_cnam
    detalhes['dst_cnam'] = chamada.dst_cnam
    detalhes['did'] = chamada.did

    detalhes['tamVar'] = len(variaveis)
    i=0
    for variavel in variaveis:
        detalhes['var'+str(i)] = variavel.variavel
        detalhes['valor' + str(i)] = variavel.valor
        i = i+1

    js_data = json.dumps(detalhes)

    return JsonResponse(js_data, safe=False)

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

    if 'variavel' in request.POST:
        variavel = request.POST['variavel']
        request.session['variavel'] = request.POST['variavel']
    else:
        variavel = request.session['variavel']
    if 'valvar' in request.POST:
        valvar = request.POST['valvar']
        request.session['valvar'] = request.POST['valvar']
    else:
        variavel = request.session['valvar']

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
    if relatorios:
        for registro in relatorios:
            horario = registro.calldate.strftime('%m/%d/%Y %H:%M:%S')
            registro.calldate = datetime.strptime(horario, '%m/%d/%Y %H:%M:%S')
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
        if campo == "cano" or campo == "cand" or variavel:
            for registro in relatorios:
                if campo == "cano" or campo == "cand":
                    if ((campo == "cano" and re.match('(.*?)'+campo_input+'(.*?)', registro.channel, re.IGNORECASE)))  or (campo == "cand" and re.match('(.*?)'+campo_input+'(.*?)', registro.dstchannel, re.IGNORECASE)):
                        if variavel:
                            if valvar:
                                variaveis = Variaveis.objects.using('relatorios').filter(variavel=variavel,uniqueid=registro.uniqueid, valor__icontains=valvar)
                            else:
                                variaveis = Variaveis.objects.using('relatorios').filter(variavel=variavel,uniqueid=registro.uniqueid)
                            if variaveis:
                                rel_filtrado.append(registro)
                        else:
                            rel_filtrado.append(registro)
                else:
                    if variavel:
                        if valvar:
                            variaveis = Variaveis.objects.using('relatorios').filter(variavel=variavel,uniqueid=registro.uniqueid, valor__icontains=valvar)
                        else:
                            variaveis = Variaveis.objects.using('relatorios').filter(variavel=variavel,uniqueid=registro.uniqueid)
                        if variaveis:
                            rel_filtrado.append(registro)

                relatorios = rel_filtrado

    data = {}
    data['dataInicioRelatorio'] = di
    data['dataFimRelatorio'] = df
    data['campo'] = campo
    data['campo_input'] = campo_input
    data['status'] = status
    variaveis = Variaveis.objects.using('relatorios').values('variavel').annotate(dcount=Count('variavel'))
    data['variaveis'] = variaveis
    data['valvar'] = valvar
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

def originados_sql():
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= CURDATE() AND ch.channel like CONCAT(\'%\' ,r.expressao , \'%\') and r.canal_id = Ca.id group by Ca.nome;")
        row = cursor.fetchall()

    return row

def destinados_sql():
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= CURDATE() AND ch.dstchannel like CONCAT(\'%\' ,r.expressao , \'%\') and r.canal_id = Ca.id group by Ca.nome;")
        row = cursor.fetchall()

    return row

def chamDia_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamDiaDest_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamDiaTodas_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamHoje_sql(todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= CURDATE() AND ca.id = r.canal_id group by ca.nome;")
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= CURDATE() AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;')
        row = cursor.fetchall()

    return row

def chamHojeDest_sql(todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= CURDATE() AND ca.id = r.canal_id group by ca.nome;")
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= CURDATE() AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;')
        row = cursor.fetchall()

    return row

def chamHojeTodas_sql(todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= CURDATE() AND ca.id = r.canal_id group by ca.nome;")
        else:
            cursor.execute('SELECT date(c.calldate) as dia,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= CURDATE() AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome;')
        row = cursor.fetchall()

    return row

def chamHora_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamHoraDest_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamHoraTodas_sql(inicioDia, fimdia, todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT hour(c.calldate) as hora,ca.nome as canal, count(c.uniqueid) as qtdChamadas from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id group by ca.nome, hour(c.calldate);', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamMin_sql(inicioDia, fimdia,todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id order by minuto, segundo;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE c.channel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id order by minuto, segundo;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamMinDest_sql(inicioDia, fimdia,todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id order by minuto, segundo;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id order by minuto, segundo;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def chamMinTodas_sql(inicioDia, fimdia,todas):
    with connections['relatorios'].cursor() as cursor:
        if todas:
            cursor.execute("SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND ca.id = r.canal_id order by minuto, segundo;", [inicioDia,fimdia])
        else:
            cursor.execute('SELECT minute(c.calldate) as minuto, second(c.calldate) as segundo, ca.nome as canal,  c.duration as duracao from Canal ca, cdr c, Regex r WHERE (c.dstchannel like CONCAT(\'%%\',r.expressao,\'%%\') OR c.channel like CONCAT(\'%%\',r.expressao,\'%%\')) AND c.calldate >= %s AND c.calldate <= %s AND c.disposition = "ANSWERED" AND ca.id = r.canal_id order by minuto, segundo;', [inicioDia,fimdia])
        row = cursor.fetchall()

    return row

def originadosdia_sql(dia):
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= %s AND ch.channel like CONCAT(\'%%\' ,r.expressao , \'%%\') and r.canal_id = Ca.id group by Ca.nome;", [dia])
        row = cursor.fetchall()

    return row

def destinadosdia_sql(dia):
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= %s AND ch.dstchannel like CONCAT(\'%%\' ,r.expressao , \'%%\') and r.canal_id = Ca.id group by Ca.nome;", [dia])
        row = cursor.fetchall()

    return row

def originadoshora_sql(diaHoraInicial,diaHoraFinal):
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= %s AND ch.calldate <= %s AND  ch.channel like CONCAT(\'%%\' ,r.expressao , \'%%\') and r.canal_id = Ca.id group by Ca.nome;", [diaHoraInicial,diaHoraFinal])
        row = cursor.fetchall()

    return row

def destinadoshora_sql(diaHoraInicial,diaHoraFinal):
    with connections['relatorios'].cursor() as cursor:
        cursor.execute("SELECT Ca.nome, COUNT(ch.uniqueid) as qtd from cdr ch,Canal Ca, Regex r WHERE ch.calldate >= %s AND ch.calldate <= %s AND ch.dstchannel like CONCAT(\'%%\' ,r.expressao , \'%%\') and r.canal_id = Ca.id group by Ca.nome;", [diaHoraInicial,diaHoraFinal])
        row = cursor.fetchall()

    return row

@login_required
def lista_graficos(request):
    originados = originados_sql()
    destinados = destinados_sql()
    canaisTudo = Canal.objects.using('relatorios').all()
    canais =[]
    for canal in canaisTudo:
        canais.append(canal.nome)

    relatorio = []
    mesAtras = date.today() - timedelta(days=30)
    while mesAtras <= date.today():
        if mesAtras ==date.today():
            linhaRel = chamHojeTodas_sql(True)
        else:
            inicioDia = datetime.combine(mesAtras, datetime.min.time())
            fimdia = datetime.combine(mesAtras, datetime.max.time())
            linhaRel = chamDiaTodas_sql(inicioDia, fimdia, True)
        linhaRelatorio = []
        linhaRelatorio.append(mesAtras.strftime("%d/%m/%Y"))
        j=0;
        tam = len(linhaRel)
        for i in range(len(canaisTudo)):
            if j< tam:
                if canaisTudo[i].nome == linhaRel[j][1]:
                    linhaRelatorio.append(linhaRel[j][2])
                    j = j +1
                else:
                    linhaRelatorio.append(0)
            else:
                linhaRelatorio.append(0)

        relatorio.append(linhaRelatorio)
        mesAtras = mesAtras + timedelta(days=1)

    originados = json.dumps(originados)
    destinados = json.dumps(destinados)
    canais = json.dumps(canais)
    relatorio = json.dumps(relatorio)

    data ={}
    data['originados'] = originados
    data['destinados'] = destinados
    data['canais'] = canais
    data['relatorio'] = relatorio
    data['diaInicio'] = date.today() - timedelta(days=30)
    data['diaAtual'] = date.today()

    return render(request, 'graficos.html',data)

@login_required
def busca_pizza(request):
    filtro = request.GET.get('filtro', None)

    if filtro == "dia":
        dia = request.GET.get('dia', None)
        originados = originadosdia_sql(dia)
        destinados = destinadosdia_sql(dia)
    else:
        if filtro =="hora":
            dia = request.GET.get('dia', None)
            hora = request.GET.get('hora', None)
            diaHoraString = dia + " " + hora
            diaHoraInicial = datetime.strptime(diaHoraString, '%Y-%m-%d %H:%M')
            diaHoraFinal = diaHoraInicial + timedelta(hours=1)
            originados = originadoshora_sql(diaHoraInicial,diaHoraFinal)
            destinados = destinadoshora_sql(diaHoraInicial,diaHoraFinal)
        else:
            if filtro == "inter":
                diaInicio = request.GET.get('data_inicio', None)
                diaFim = request.GET.get('data_fim', None)
                originados = originadoshora_sql(diaInicio,diaFim)
                destinados = destinadoshora_sql(diaInicio,diaFim)

    data ={}
    data['originados'] = originados
    data['destinados'] = destinados
    js_data = json.dumps(data)

    return JsonResponse(js_data, safe=False)

@login_required
def busca_linha(request):
    filtro = request.GET.get('apurar', None)
    status = request.GET.get('status', None)
    cham = request.GET.get('chamadas', None)

    if status == "todas":
        todas = True
    else:
        todas = False
    canaisTudo = Canal.objects.using('relatorios').all()
    canais =[]
    for canal in canaisTudo:
        canais.append(canal.nome)

    relatorio = []
    if filtro == "dia":
        diaInicio = datetime.strptime(request.GET.get('data_inicioR', None), "%Y-%m-%d")
        diaFim = datetime.strptime(request.GET.get('data_fimR', None), "%Y-%m-%d")

        while diaInicio <= diaFim:
            if diaInicio ==date.today():
                if cham == "todas":
                    linhaRel = chamHojeTodas_sql(todas)
                else:
                    if cham == "originadas":
                        linhaRel = chamHoje_sql(todas)
                    else:
                        linhaRel = chamHojeDest_sql(todas)
            else:
                inicioDia = datetime.combine(diaInicio, datetime.min.time())
                fimdia = datetime.combine(diaInicio, datetime.max.time())
                if cham == "todas":
                    linhaRel = chamDiaTodas_sql(inicioDia, fimdia,todas)
                else:
                    if cham == "originadas":
                        linhaRel = chamDia_sql(todas)
                    else:
                        linhaRel = chamDiaDest_sql(todas)
            linhaRelatorio = []
            linhaRelatorio.append(diaInicio.strftime("%d/%m/%Y"))
            j=0;
            tam = len(linhaRel)
            for i in range(len(canaisTudo)):
                if j< tam:
                    if canaisTudo[i].nome == linhaRel[j][1]:
                        linhaRelatorio.append(linhaRel[j][2])
                        j = j +1
                    else:
                        linhaRelatorio.append(0)
                else:
                    linhaRelatorio.append(0)

            relatorio.append(linhaRelatorio)
            diaInicio = diaInicio + timedelta(days=1)
    else:
        if filtro =="hora":
            diaInicio = datetime.strptime(request.GET.get('data_inicioR', None), "%Y-%m-%d")

            inicioDia = datetime.combine(diaInicio, datetime.min.time())
            fimdia = datetime.combine(diaInicio, datetime.max.time())
            if cham == "todas":
                linhaRel = chamHoraTodas_sql(inicioDia, fimdia, todas)
            else:
                if cham == "originadas":
                    linhaRel = chamHora_sql(inicioDia, fimdia, todas)
                else:
                    linhaRel = chamHoraDest_sql(inicioDia, fimdia, todas)
            relatorio = []
            hora = 0
            while hora <24:
                linhaRelatorio = []
                linhaRelatorio.append(str(hora) +":00")
                j=0;
                tam = len(linhaRel)

                for canal in canaisTudo:
                    k= 1
                    for i in range(len(linhaRel)):
                        if hora == int(linhaRel[i][0]):
                            if linhaRel[i][1] == canal.nome:
                                linhaRelatorio.append(linhaRel[i][2])
                                break
                            else:
                                if k==tam:
                                    linhaRelatorio.append(0)
                        else:
                            if k==tam:
                                linhaRelatorio.append(0)

                        k = k + 1
                relatorio.append(linhaRelatorio)
                hora = hora + 1
        else:
            if filtro == "min":
                diaInicio = request.GET.get('data_inicioR', None)
                horaInicio = request.GET.get('horaR', None)
                inicioDia= diaInicio + " " +horaInicio

                inicioDia = datetime.strptime(inicioDia, "%Y-%m-%d %H:%M")
                fimdia = inicioDia.replace(minute=59, second=59)
                if cham == "todas":
                    linhaRel = chamMinTodas_sql(inicioDia, fimdia,todas)
                else:
                    if cham == "originadas":
                        linhaRel = chamMin_sql(inicioDia, fimdia,todas)
                    else:
                        linhaRel = chamMinDest_sql(inicioDia, fimdia,todas)
                for i in range(len(linhaRel)):
                    min = linhaRel[i][0]
                    seg = linhaRel[i][1]

                    duracao = timedelta(seconds=linhaRel[i][3])
                    tempo = inicioDia.replace(minute=min, second=seg)
                    total = tempo + duracao

                    if int(total.minute) > min:
                        min = min + 1
                        while min <= int(total.minute):
                            linhaRel = linhaRel + ((min,0,linhaRel[i][2],0),)
                            min = min + 1

                tam = len(linhaRel)
                relatorio = []
                min = 0
                while min <60:
                    linhaRelatorio = []
                    if min < 10:
                        min = "0" + str(min)
                    linhaRelatorio.append(str(inicioDia.hour) +":" + str(min))

                    countCham =0
                    for canal in canaisTudo:
                        countCham =0
                        for i in range(len(linhaRel)):
                            if int(min) == int(linhaRel[i][0]):
                                if linhaRel[i][2] == canal.nome:
                                    countCham = countCham + 1
                        linhaRelatorio.append(countCham)

                    relatorio.append(linhaRelatorio)
                    min = int(min) +1

    data ={}
    data['relatorio'] = relatorio
    data['canais'] = canais
    js_data = json.dumps(data)

    return JsonResponse(js_data, safe=False)

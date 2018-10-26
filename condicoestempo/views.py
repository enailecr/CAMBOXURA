from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import CondicaoTempo, GrupoTempo
import re
from django_tables2 import RequestConfig
from .tables import CondicaoTempoTable


@login_required
def add(request):
    return render(request, 'CadastroCondicoesTempo.html')

@login_required
def list(request):
    table = CondicaoTempoTable(GrupoTempo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'condicoesTempo.html',{'table': table})

@login_required
def condicoestempo_novo(request):
    #nome = request.POST['nome']
    horaInicio = request.POST['hora_inicio']
    horaFim = request.POST['hora_termino']
    diaSemanaInicio = request.POST['dia_semana_ini']
    diaSemanaFim = request.POST['dia_semana_ter']
    diaMesInicio = request.POST['dia_mes_inicio']
    diaMesFim = request.POST['dia_mes_termina']
    mesIncio = request.POST['mes_inicio']
    mesFim = request.POST['mes_termino']

    #destino = request.POST['nome']   
    condicoestempo = GrupoTempo( horaInicio=horaInicio,horaFim=horaFim, diaSemanaInicio=diaSemanaInicio,
    diaSemanaFim=diaSemanaFim, diaMesInicio=diaMesInicio, diaMesFim= diaMesFim,mesIncio=mesIncio,mesFim=mesFim)
    condicoestempo.save()
    return redirect ('/condicoestempo/')

@login_required
def condicoestempo_edita(request, id):
    data = {}
    condicoestempo = CondicaoTempo.objects.get(id=id)
    data['condicoestempo'] = condicoestempo
    if request.method == 'POST':
        condicoestempo = CondicaoTempo.objects.get(id=id)
    
        nome = request.POST['nome']
        horaInicio = request.POST['hora_inicio']
        horaFim = request.POST['hora_termino']
        diaSemanaInicio = request.POST['dia_semana_ini']
        diaSemanaFim = request.POST['dia_semana_ter']
        diaMesInicio = request.POST['dia_mes_inicio']
        diaMesFim = request.POST['dia_mes_termina']
        mesIncio = request.POST['mes_inicio']
        mesFim = request.POST['mes_termino']
        #destino = request.POST['nome'] 
        
        condicoestempo.nome= nome
        condicoestempo.horaInicio = horaInicio
        condicoestempo.horaFim = horaFim
        condicoestempo.diaSemanaInicio = diaSemanaInicio
        condicoestempo.diaSemanaFim = diaSemanaFim
        condicoestempo.diaMesInicio = diaMesInicio
        condicoestempo.diaMesFim = diaMesFim
        condicoestempo.mesIncio = mesIncio
        condicoestempo.mesFim = mesFim

        condicoestempo.save()        
        return redirect('/condicoestempo/')
    else:
        return render(request, 'editaCondicaoTempo.html', data)


@login_required
def condicoestempo_remove(request, id):
    condicoestempo = CondicaoTempo.objects.get(id=id)
    condicoestempo.delete()
    return redirect('/condicoestempo/')

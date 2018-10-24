from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NumeroEntrada
from django.contrib.auth.decorators import login_required
import re
from django_tables2 import RequestConfig
from .tables import NumeroTable

@login_required
def add(request):
    return render(request, 'CadastroNumero.html')

@login_required
def list(request):
    table = NumeroTable(NumeroEntrada.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'num.html', {'table': table})

# @login_required
# def dispositivo_busca(request):
#     dispositivos = Dispositivo.objects.all()
#     filter = request.GET.get('search')
#     if filter:
#         disp = []
#         for dispositivo in dispositivos:
#             if re.search(filter, dispositivo.unidade.sigla, re.IGNORECASE):
#                 disp.append(dispositivo)
#         dispositivos = disp
#     table = DispositivoTable(dispositivos)
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#     return render(request, 'menu-3d.html', {'table': table})

@login_required
def numero_novo(request):
    numero = request.POST['numero']
    origem = request.POST['origem']
    if 'atendido' in request.POST: 
        atendido = request.POST['atendido']
    else:
        atendido = False
    if 'grava_chamada' in request.POST:   
        gravaChamada = request.POST['grava_chamada']
    else:
        gravaChamada = False
    #destino = request.POST['nome']

    numeroEntrada = NumeroEntrada(numero=numero, origem = origem, atendido=atendido, gravaChamada=gravaChamada)

    # form = NumeroEntradaForm(request.POST or None)
    # if form.is_valid():
    numeroEntrada.save()
    return redirect ('/numeros/')

@login_required
def numero_edita(request, id):
    data = {}
    
    numero = NumeroEntrada.objects.get(id=id)
    data['numero'] = numero
    if request.method == 'POST':
        numero = NumeroEntrada.objects.get(id=id)
        origem = request.POST['origem']
        if 'atendido' in request.POST: 
                atendido = request.POST['atendido']
        else:
                atendido = False
        if 'grava_chamada' in request.POST:   
                gravaChamada = request.POST['grava_chamada']
        else:
                gravaChamada = False

        numero.origem = origem
        numero.atendido = atendido
        numero.gravaChamada = gravaChamada
        numero.save()        
        return redirect('/numeros/')
        
    else:
        return render(request, 'editaNumero.html', data)

@login_required
def numero_remove(request, id):
    numero = NumeroEntrada.objects.get(id=id)
    numero.delete()
    return redirect('/numeros/')

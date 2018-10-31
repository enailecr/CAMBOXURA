from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import URA 
import re
from django_tables2 import RequestConfig
from .tables import URATable


@login_required
def add(request):
    return render(request, 'UraNovo.html')

@login_required
def list(request):
    table = URATable(URA.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'uras.html', {'table': table})

@login_required
def ura_novo(request):
    nome = request.POST['descricao']
    descricao = request.POST['descricao']
    anuncioUra = request.POST['descricao']
    discarDireto = request.POST['descricao']
    timeout = request.POST['descricao']
    tentativasInvalidas = request.POST['descricao']
    gravRepetInvalid = request.POST['descricao']

    if 'descricao' in request.POST: 
        anexAnuncInvalid = request.POST['descricao']
    else:
        anexAnuncInvalid = False

    if 'descricao' in request.POST: 
        returnInvalid = request.POST['descricao']
    else:
        returnInvalid = False

    gravInvalid =request.POST['descricao']
    # destinoInvalid = models.OneToOneField(
    #     Destino,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     related_name= 'destinoInvalidURA'
    # )
    retentativasTimeout = request.POST['descricao']
    gravRetentTimeout = request.POST['descricao']
    if 'descricao' in request.POST: 
        anexAnuncTimeout = request.POST['descricao']
    else:
        anexAnuncTimeout = False

    if 'descricao' in request.POST: 
        retornarTimeout = request.POST['descricao']
    else:
        retornarTimeout = False
    
    gravTimeout = request.POST['descricao']
    # destinoTimeout = models.OneToOneField(
    #     Destino,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     related_name='destinoTimeoutURA'
    # )
    if 'descricao' in request.POST: 
        returnURACaixaPostal = request.POST['descricao']
    else:
        returnURACaixaPostal = False

    ura = URA(nome=nome,descricao=descricao,anuncioUra=anuncioUra, discarDireto=discarDireto,
    timeout=timeout,tentativasInvalidas=tentativasInvalidas,gravRepetInvalid=gravRepetInvalid,
    anexAnuncInvalid=anexAnuncInvalid,returnInvalid=returnInvalid,gravInvalid=gravInvalid,
    retentativasTimeout=retentativasTimeout,gravRetentTimeout=gravRetentTimeout,
    anexAnuncTimeout=anexAnuncTimeout,retornarTimeout=retornarTimeout,gravTimeout=gravTimeout,
    returnURACaixaPostal=returnURACaixaPostal)
    ura.save() 
    return redirect ('/uras/')

@login_required
def ura_edita(request, id):
    data = {}
    ura = URA.objects.get(id=id)
    data['ura'] = ura
    if request.method == 'POST':
           
        return redirect('/uras/')
    else:
        return render(request, 'editaUra.html', data)


@login_required
def ura_remove(request, id):
    ura = URA.objects.get(id=id)
    ura.delete()
    return redirect('/uras/')

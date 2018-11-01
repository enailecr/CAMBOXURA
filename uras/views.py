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
    nome = request.POST['nome']
    descricao = request.POST['descricao']
    anuncioUra = request.POST['anuncio']
    #discarDireto = request.POST['descricao']
    timeout = request.POST['timeout']
    tentativasInvalidas = request.POST['tent_inv']
    gravRepetInvalid = request.POST['invrerecor']

    if 'app_ann_inv' in request.POST: 
        anexAnuncInvalid = request.POST['app_ann_inv']
    else:
        anexAnuncInvalid = False

    if 'ReturnInvalid' in request.POST: 
        returnInvalid = request.POST['ReturnInvalid']
    else:
        returnInvalid = False

    gravInvalid =request.POST['gravinvalid']
    # destinoInvalid = models.OneToOneField(
    #     Destino,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     related_name= 'destinoInvalidURA'
    # )
    retentativasTimeout = request.POST['timeout_ret']
    gravRetentTimeout = request.POST['timeout_record']
    if 'descappend_anon_timoutricao' in request.POST: 
        anexAnuncTimeout = request.POST['append_anon_timout']
    else:
        anexAnuncTimeout = False

    if 'return_timout' in request.POST: 
        retornarTimeout = request.POST['return_timout']
    else:
        retornarTimeout = False
    
    gravTimeout = request.POST['timeout_record']
    # destinoTimeout = models.OneToOneField(
    #     Destino,
    #     on_delete=models.CASCADE,
    #     parent_link=True,
    #     related_name='destinoTimeoutURA'
    # )
    if 'append_anon_timout' in request.POST: 
        returnURACaixaPostal = request.POST['append_anon_timout']
    else:
        returnURACaixaPostal = False
    #discarDireto=discarDireto,
    ura = URA(nome=nome,descricao=descricao, 
    timeout=timeout,tentativasInvalidas=tentativasInvalidas,
    anexAnuncInvalid=anexAnuncInvalid,returnInvalid=returnInvalid,
    retentativasTimeout=retentativasTimeout,
    anexAnuncTimeout=anexAnuncTimeout,retornarTimeout=retornarTimeout,
    returnURACaixaPostal=returnURACaixaPostal)
    ura.save() 
    anuncio= Anuncio(gravTimeout=gravTimeout,gravRetentTimeout=gravRetentTimeout,gravInvalid=gravInvalid,gravRepetInvalid=gravRepetInvalid,anuncioUra =anuncioUra )
    anuncio.save()
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

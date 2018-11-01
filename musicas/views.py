from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Musica, Streaming , MusicaCategoria
import re
from django_tables2 import RequestConfig
from .tables import MusicaTable

@login_required
def addcategoria(request):
    return render(request, 'CadastroMusica.html')

@login_required
def addstreaming(request):
    return render(request, 'CadastroStreaming.html')

@login_required
def list(request):
    table = MusicaTable(Musica.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'musicas.html', {'table': table})

@login_required
def categoria_novo(request):
    nome = request.POST['nome']
    
    if 'exerand' in request.POST: 
        execRandom = request.POST['exerand']
    else:
        execRandom = False
    musica = Musica(nome=nome)
    musicaCategoria = MusicaCategoria(execRandom=execRandom)
    musicaCategoria.save()
    musica.save()
    return redirect ('/musicas/')

@login_required
def streaming_novo(request):
    aplicacao = request.POST['apl']
    formato = request.POST['form']
    streaming = Streaming(aplicacao=aplicacao,formato=formato)
    streaming.save()
    return redirect ('/musicas/')

@login_required
def musica_edita(request, id):
    data = {}
    musica = Musica.objects.get(id=id)
    data['Musica'] = musica

    if request.method == 'POST':
        nome = request.POST['nome']
        if 'exerand' in request.POST: 
            execRandom = request.POST['exerand']
        else:
            execRandom = False
        musica.nome = nome
        musicaCategoria.execRandom = execRandom
        musicaCategoria.save()
        musica.save()       
        return redirect('/musicas/')
    else:
        return render(request, 'editaMusica.html', data)

   

@login_required
def musica_remove(request, id):
    musica = Musica.objects.get(id=id)
    musica.delete()
    return redirect('/musicas/')
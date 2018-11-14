from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Musica, Streaming , MusicaCategoria
import re
from django_tables2 import RequestConfig
from .tables import MusicaTable
from django.core.files.storage import FileSystemStorage
from anuncios.models import Gravacao

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
    volume = request.POST['volume']

    if 'exerand' in request.POST:
        execRandom = request.POST['exerand']
    else:
        execRandom = False

    musicaCategoria = MusicaCategoria(execRandom=execRandom, nome=nome, volume=volume)
    musicaCategoria.save()

    myfile = request.FILES['anexMusica']
    nome = request.POST['nomeGravacao']
    gravacaoid = upload_file_cad(myfile, nome);
    gravacao = Gravacao.objects.get(id=gravacaoid)
    gravacao.musica= musicaCategoria
    gravacao.save()

    return redirect ('/musicas/')

@login_required
def streaming_novo(request):
    aplicacao = request.POST['apl']
    formato = request.POST['form']
    nome = request.POST['nome']
    streaming = Streaming(aplicacao=aplicacao,formato=formato)
    streaming.save()
    return redirect ('/musicas/')

@login_required
def musica_edita(request, id):
    data = {}
    #musica = Musica.objects.get(id=id)

    try:
        musica=MusicaCategoria.objects.get(id=id)
        gravacoes = Gravacao.objects.filter(musica__exact=musica)
        data['gravacoes'] = gravacoes
        categoria=True
    except MusicaCategoria.DoesNotExist:
        musica = Streaming.objects.get(id=id)
        categoria=False
    data['streaming'] = musica

    if request.method == 'POST':
        nome = request.POST['nome']
        if 'apl' in request.POST:
            aplicacao = request.POST['apl']
            formato = request.POST['form']
            musica.aplicacao = aplicacao
            musica.nome = nome
            musica.formato = formato
            musica.save()
        else:
            if 'exerand' in request.POST:
                execRandom = request.POST['exerand']
            else:
                execRandom = False
            musica.nome = nome
            musica.execRandom = execRandom
            musica.save()

            if 'anexMusica' in request.FILES:
                myfile = request.FILES['anexMusica']
                nome = request.POST['nomeGravacao']
                gravacaoid = upload_file_cad(myfile, nome);
                gravacao = Gravacao.objects.get(id=gravacaoid)
                gravacao.musica= musica
                gravacao.save()

        return redirect('/musicas/')
    else:
        if categoria:
            return render(request, 'editaMusica.html', data)
        else:
            return render(request, 'editaStreaming.html', data)



@login_required
def musica_remove(request, id):
    musica = Musica.objects.get(id=id)
    fs = FileSystemStorage()
    gravacoes = Gravacao.objects.filter(musica__exact=musica)
    for gravacao in gravacoes:
        fs.delete(gravacao.link)
        gravacao.delete()
    musica.delete()
    return redirect('/musicas/')

def upload_file_cad(myfile, nome):

    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)

    gravacao = Gravacao(nome=nome, link=filename)
    gravacao.save()
    return gravacao.id

def gravacao_remove(gravacao, id):
    gravacao = Gravacao.objects.get(id=id)
    fs = FileSystemStorage()
    gravacoes = Gravacao.objects.filter(musica__exact=musica)
    for gravacao in gravacoes:
        fs.delete(gravacao.link)
        gravacao.delete()
    gravacao.delete()
    return redirect('/musicas/')

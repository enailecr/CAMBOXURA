from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Musica, Streaming , MusicaCategoria
import re
from django_tables2 import RequestConfig
from .tables import MusicaTable
from django.core.files.storage import FileSystemStorage
from anuncios.models import Gravacao
from django.core.exceptions import ObjectDoesNotExist

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
    try:
        gravacoes = Gravacao.objects.get(musica=musicaCategoria)
    except ObjectDoesNotExist:
        gravacoes = None
    data = {}
    data['musica'] = musicaCategoria
    data['gravacoes'] = gravacoes

    return render(request, 'CadastroMusica2.html', data)

@login_required
def streaming_novo(request):
    aplicacao = request.POST['apl']
    formato = request.POST['form']
    nome = request.POST['nome']
    streaming = Streaming(aplicacao=aplicacao,formato=formato, nome=nome)
    streaming.save()
    return redirect ('/musicas/')

@login_required
def musica_edita(request, id):
    data = {}

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
        if categoria is False:
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

            volume = request.POST['volume']
            musica.nome = nome
            musica.execRandom = execRandom
            musica.volume = volume
            musica.save()
        if categoria:
            gravacoes = Gravacao.objects.filter(musica__exact=musica)
            data['gravacoes'] = gravacoes
            return render(request, 'editaMusica.html', data)
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
        fs.delete("../"+gravacao.link)
        gravacao.delete()
    musica.delete()
    return redirect('/musicas/')

@login_required
def upload_file_cad(request , id):
    if request.method == 'POST':
        musica = MusicaCategoria.objects.get(id=id)
        myfile = request.FILES['anexGravacao']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        nome = request.POST['nomeGravacao']
        tipo = '2'
        gravacao = Gravacao(nome=nome, link=uploaded_file_url, tipo=tipo, musica=musica)
        gravacao.save()

        gravacoes = Gravacao.objects.filter(musica__exact=musica)
        data = {}
        data['musica'] = musica
        data['gravacoes'] = gravacoes
        return render(request, 'CadastroMusica2.html', data)

@login_required
def gravacao_remove(request, id):
    gravacao = Gravacao.objects.get(id=id)
    musica = gravacao.musica
    fs = FileSystemStorage()
    fs.delete("../"+gravacao.link)
    gravacao.delete()
    data = {}
    data['streaming'] = musica
    gravacoes = Gravacao.objects.filter(musica__exact=musica)
    data['gravacoes'] = gravacoes
    return render(request, 'editaMusica.html', data)

@login_required
def upload_file_edt(request , id):
    if request.method == 'POST':
        musica = MusicaCategoria.objects.get(id=id)
        myfile = request.FILES['anexGravacao']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        nome = request.POST['nomeGravacao']
        tipo = '2'
        gravacao = Gravacao(nome=nome, link=uploaded_file_url, tipo=tipo, musica=musica)
        gravacao.save()

        gravacoes = Gravacao.objects.filter(musica__exact=musica)
        data = {}
        data['streaming'] = musica
        data['gravacoes'] = gravacoes
        return render(request, 'editaMusica.html', data)

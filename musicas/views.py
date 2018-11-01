from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StreamingForm, MusicaForm
from .models import Musica, Streaming
import re
from django_tables2 import RequestConfig
from .tables import MusicaTable

@login_required
def addcategoria(request):
    form = MusicaForm()
    data = {'form' : form}
    return render(request, 'CadastroMusica.html', data)

@login_required
def addstreaming(request):
    form = StreamingForm()
    data = {'form' : form}
    return render(request, 'CadastroStreaming.html', data)

@login_required
def list(request):
    table = MusicaTable(Musica.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'musicas.html', {'table': table})

@login_required
def categoria_novo(request):
    form = MusicaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/musicas/')@login_required

@login_required
def streaming_novo(request):
    form = StreamingForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/musicas/')

@login_required
def musica_edita(request, id):
    data = {}
    musica = Musica.objects.get(id=id)
    form = MusicaForm(request.POST or None, instance=musica)
    data['streaming'] = musica
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/musicas/')
    else:
        return render(request, 'editaMusica.html', data)

    if 'exerand' in request.POST: 
        anexAnuncInvalid = request.POST['exerand']
    else:
        anexAnuncInvalid = False

@login_required
def musica_remove(request, id):
    musica = Musica.objects.get(id=id)
    musica.delete()
    return redirect('/musicas/')
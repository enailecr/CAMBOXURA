from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AnuncioForm
from .models import Anuncio 
import re
from django_tables2 import RequestConfig
from .tables import AnuncioTable

@login_required
def add(request):
    form = AnuncioForm()
    data = {'form' : form}
    return render(request, 'CadastroAnuncio.html', data)

@login_required
def list(request):
    table = AnuncioTable(Anuncio.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'anuncios.html',{'table': table})

@login_required
def anuncio_novo(request):
    form = AnuncioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/anuncios/')
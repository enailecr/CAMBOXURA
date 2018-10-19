from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AnuncioForm

@login_required
def add(request):
    form = AnuncioForm()
    data = {'form' : form}
    return render(request, 'CadastroAnuncio.html', data)

@login_required
def list(request):
    return render(request, 'anuncios.html')

@login_required
def anuncio_novo(request):
    form = AnuncioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/anuncios/')
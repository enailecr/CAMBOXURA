from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CondicaoTempoForm


@login_required
def add(request):
    form = CondicaoTempoForm()
    data = {'form' : form}
    return render(request, 'CadastroCondicoesTempo.html', data)

@login_required
def list(request):
    return render(request, 'condicoesTempo.html')

@login_required
def condicoestempo_novo(request):
    form = CondicaoTempoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/condicoestempo/')
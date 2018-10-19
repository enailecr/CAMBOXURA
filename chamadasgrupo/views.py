from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ChamadaEmGrupoForm


@login_required
def add(request):
    form = ChamadaEmGrupoForm()
    data = {'form' : form}
    return render(request, 'CadastroChamadasGrupo.html', data)

@login_required
def list(request):
    return render(request, 'ringGroup.html')

@login_required
def chamadasgrupo_novo(request):
    form = ChamadaEmGrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/chamadasgrupo/')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ChamadaEmGrupoForm
from .models import ChamadaEmGrupo 
import re
from django_tables2 import RequestConfig
from .tables import ChamadaEmGrupoTable

@login_required
def add(request):
    form = ChamadaEmGrupoForm()
    data = {'form' : form}
    return render(request, 'CadastroChamadasGrupo.html', data)

@login_required
def list(request):
    table = ChamadaEmGrupoTable(ChamadaEmGrupo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'ringGroup.html',{'table': table})

@login_required
def chamadasgrupo_novo(request):
    form = ChamadaEmGrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/chamadasgrupo/')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FilaForm
from .models import Fila 
import re
from django_tables2 import RequestConfig
from .tables import FilaTable


@login_required
def add(request):
    form = FilaForm()
    data = {'form' : form}
    return render(request, 'CadastroFila.html', data)

@login_required
def list(request):
    table = FilaTable(Fila.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'filas.html',{'table': table})

@login_required
def fila_novo(request):
    form = FilaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/filas/')
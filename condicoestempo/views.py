from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CondicaoTempoForm
from .models import CondicaoTempo 
import re
from django_tables2 import RequestConfig
from .tables import CondicaoTempoTable


@login_required
def add(request):
    form = CondicaoTempoForm()
    data = {'form' : form}
    return render(request, 'CadastroCondicoesTempo.html', data)

@login_required
def list(request):
    table = CondicaoTempoTable(CondicaoTempo.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'condicoesTempo.html',{'table': table})

@login_required
def condicoestempo_novo(request):
    form = CondicaoTempoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/condicoestempo/')
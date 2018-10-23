from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UraForm
from .models import URA 
import re
from django_tables2 import RequestConfig
from .tables import URATable


@login_required
def add(request):
    form = UraForm()
    data = {'form' : form}
    return render(request, 'UraNovo.html', data)

@login_required
def list(request):
    table = URATable(URA.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'uras.html', {'table': table})

@login_required
def ura_novo(request):
    form = UraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/uras/')
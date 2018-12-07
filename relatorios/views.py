from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Relatorios, Cdr
import re
from django_tables2 import RequestConfig
from .tables import RelatoriosTable
@login_required
def list(request):
    relatorios = Cdr.objects.using('relatorios').all()
    table = RelatoriosTable(relatorios)
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'relatorios.html',{'table': table})

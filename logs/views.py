from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import re
from django_tables2 import RequestConfig
from .forms import LogsForm
from .tables import LogsTable
from .models import Log

@login_required
def list(request):

    table = LogsTable(Log.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'logs.html',{'table': table})

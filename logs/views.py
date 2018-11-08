from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import re
from django_tables2 import RequestConfig

@login_required
def list(request):
    
    return render(request, 'logs.html',{'table': table})


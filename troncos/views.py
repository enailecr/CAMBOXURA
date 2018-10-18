from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def list(request):
    return render(request, 'troncos.html')

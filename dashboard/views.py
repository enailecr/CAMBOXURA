from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Dashboard
@login_required
def list(request):
    data = {}
    todos = Dashboard.objects.all()
    cont=len(todos) - 1
    dashboard=todos[cont]
    data['dashboard'] = dashboard
    data['todos'] = todos
    #valor referente a um mes de dados
    # if len(todos) < 21600:
    #     n=21600 - len(todos)
    #     for i in range(n):

            # todos[i].minute=0
            # todos[i].hour=0
            # todos[i].day=0
            # todos[i].month=0
            # todos[i].year=0
            # todos[i].RAMU=0
            # todos[i].RAMF=0
            # todos[i].SWAP=0 
            # todos[i].SWAPF=0
            # todos[i].SWAPU=0
            # todos[i].RAM=0
            # todos[i].CPU=0
            # todos[i].discoUsado=0
            # todos[i].discoLivre=0
            # todos[i].capacidadeDisco=0
    return render(request, 'dashboard.html',data)

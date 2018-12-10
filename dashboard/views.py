from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Dashboard
import datetime

@login_required
def list(request):
        data = {}
        todos = Dashboard.objects.all()
        cont=len(todos) - 1
        dashboard=todos[cont]
        data['dashboard'] = dashboard
        data['todos'] = todos
        lista = {}
        if len(todos) < 21600:
                n=21600 - len(todos)
                grafico = Dashboard.objects.all().order_by('-timestamp')
        else:    
                grafico = Dashboard.objects.all().order_by('-timestamp')[:21600]
                # if n:
                #      primeiro_dia = grafico.order_by('timestamp')[0]
                #      primeiro_dia.timestamp
                #      hoje= datetime.now()
                
                # else:
        grafico_ordenado = grafico.order_by('timestamp')   
        for i in range(len(grafico)):
                data['gtes'+str(i)] = grafico_ordenado[i]        
        #data['grafico'] = grafico_ordenado
        return render(request, 'dashboard.html',data)

#     for j in range(12):
#         lista.append([])

#     if len(todos) < 21600:
#         n=21600 - len(todos)
        # for j in range(n):
        #         for w in range(12):
        #         lista[w].append(0)
#         for i in range(len(todos)):
#                 lista[0].append(todos[i].minute)
#                 lista[1].append(todos[i].hour)
#                 lista[2].append(todos[i].day)
#                 lista[3].append(todos[i].month)
#                 lista[4].append(todos[i].year)
#                 lista[5].append(todos[i].RAMU)
#                 lista[6].append(todos[i].RAMF)
#                 lista[7].append(todos[i].SWAPF)
#                 lista[8].append(todos[i].SWAPU)
#                 lista[9].append(todos[i].discoUsado)
#                 lista[10].append(todos[i].discoLivre)
#                 lista[11].append(todos[i].CPU)
           
            
    #valor referente a um mes de dados
#     if len(todos) < 21600:
#         n=21600 - len(todos)
#         for i in range(n):

        #     todos[i].minute=0
        #     todos[i].hour=0
        #     todos[i].day=0
        #     todos[i].month=0
        #     todos[i].year=0
        #     todos[i].RAMU=0
        #     todos[i].RAMF=0
        #     todos[i].SWAP=0 
        #     todos[i].SWAPF=0
        #     todos[i].SWAPU=0
        #     todos[i].RAM=0
        #     todos[i].CPU=0
        #     todos[i].discoUsado=0
        #     todos[i].discoLivre=0
        #     todos[i].capacidadeDisco=0
    

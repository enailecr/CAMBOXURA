from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Dashboard
from django.db.models import Avg, Max, Min, Sum, Count
from django.db.models import Count
import datetime
from django.http import JsonResponse
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder
import simplejson


# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models.utils import list_to_queryset
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
        grafico_ordenado = grafico_ordenado.values_list('day', 'month', 'year').annotate(CPU_MAX=Max('CPU'), CPU_AVG=Avg('CPU'),CPU_MIN=Min('CPU'),RAM_MAX=Max('RAM'), RAM_AVG=Avg('RAM'),RAM_MIN=Min('RAM'),SWAP_MAX=Max('SWAP'), SWAP_AVG=Avg('SWAP'),SWAP_MIN=Min('SWAP'),disco_MAX=Max('disco'), disco_AVG=Avg('disco'),disco_MIN=Min('disco')).order_by('day', 'month', 'year')
        # .filter(day=0)
        teste = grafico_ordenado.aggregate(Max('CPU'),Max('RAM'),Max('SWAP'),Max('disco'),Min('CPU'),Min('RAM'),Min('SWAP'),Min('disco'),Avg('CPU'),Avg('RAM'),Avg('SWAP'),Avg('disco'))
        # for i in range(grafico):  
        i=1
        #teste=grafico_ordenado[i]
        # output = serializers.serialize('json', grafico_ordenado)

        # temp_output = serializers.serialize('python', grafico_ordenado)
        # output = json.dumps(temp_output, cls=DjangoJSONEncoder)
        # json_serialized_objects = serializers.serialize("json", grafico_ordenado)
        #lists = grafico_ordenado.(query)
        # json_posts = json.dumps(list(posts))
        lista=[]
        lista1=[]
        # datass = serializers.serialize('json', list(grafico_ordenado))

        # data = json.dumps(list(grafico_ordenado))
        # prices_json = json.dumps(list(grafico_ordenado), cls=DjangoJSONEncoder)
        # prices_json = json.dumps(list(grafico_ordenado), cls=DjangoJSONEncoder)
        # django_list = list(grafico_ordenado)
        #json_list = simplejson.dumps(grafico_ordenado)

        #teste = [1,2,3]
        # teste=str(teste).strip('[]')
        
        teste=str(grafico_ordenado)
        teste= teste[12:-3]
        teste = teste.replace("(","")
        teste = teste.split("),")
        teste = str(teste).strip('[]')
        teste = teste[1:-1]
        teste = teste.replace("', '","zz")
        aaa= teste
        
        # json_posts = json.dumps(list(grafico_ordenado))
        # grafico_ordenado = lista.append(grafico_ordenado.values())
        # queryset = list_to_queryset(grafico_ordenado)
        data['gtes'+str(i)] = aaa        
        data['grafico'] = grafico_ordenado
        j=0
        # lista=[]
        # lista.append(grafico_ordenado[j].CPU)
        # lista.append(grafico_ordenado[j].RAM)
        # lista.append(grafico_ordenado[j].SWAP)
        # lista.append(grafico_ordenado[j].disco)


        # for i in range (len(grafico)):
        #         if j==i:
        #                 diacomeca = grafico_ordenado[j].day  
        #                 conta = 0
        #                 maxcpu = grafico_ordenado[j].CPU
        #                 mincpu = maxcpu
        #                 maxram = grafico_ordenado[j].RAM
        #                 minram = maxram
        #                 maxswap = grafico_ordenado[j].SWAP
        #                 minswap = maxswap
        #                 maxdisco = grafico_ordenado[j].disco
        #                 mindisco = maxdisco
        #                 for j in range (len(grafico)):
        #                         if j>=i:
        #                                 if diacomeca == grafico_ordenado[j].day:
        #                                         lista[0] = lista[0] + grafico_ordenado[j].CPU
        #                                         lista[1] = lista[1] + grafico_ordenado[j].RAM
        #                                         lista[2] = lista[2] + grafico_ordenado[j].SWAP
        #                                         lista[3] = lista[3] + grafico_ordenado[j].disco
        #                                         conta = conta + 1
        #                                         if maxcpu < grafico_ordenado[j].CPU:
        #                                                 maxcpu = grafico_ordenado[j].CPU
        #                                         if maxram < grafico_ordenado[j].RAM:
        #                                                 maxram = grafico_ordenado[j].RAM
        #                                         if maxswap < grafico_ordenado[j].SWAP:
        #                                                 maxswap = grafico_ordenado[j].SWAP
        #                                         if maxdisco < grafico_ordenado[j].disco:
        #                                                 maxdisco = grafico_ordenado[j].disco
        #                                         if mincpu > grafico_ordenado[j].CPU:
        #                                                 mincpu = grafico_ordenado[j].CPU
        #                                         if minram > grafico_ordenado[j].RAM:
        #                                                 minram = grafico_ordenado[j].RAM
        #                                         if minswap > grafico_ordenado[j].SWAP:
        #                                                 minswap = grafico_ordenado[j].SWAP
        #                                         if mindisco > grafico_ordenado[j].disco:
        #                                                 mindisco = grafico_ordenado[j].disco
        #                                 else:
        #                                         break                                                                                                   
        #                 lista[0] = lista[0]/conta
        #                 lista[1] = lista[1]/conta
        #                 lista[2] = lista[2]/conta
        #                 lista[3] = lista[3]/conta
        #                 lista.append(maxcpu)
        #                 lista.append(mincpu)
        #                 lista.append(maxram)
        #                 lista.append(minram)
        #                 lista.append(maxswap)
        #                 lista.append(minswap)
        #                 lista.append(maxdisco)
        #                 lista.append(mindisco)
        #                 data[diacomeca] = lista


        # for i in range(len(grafico)):
        #         data['gtes'+str(i)] = grafico_ordenado[i]        
        
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
    

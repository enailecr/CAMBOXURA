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
from django.contrib.admin.views.decorators import staff_member_required

# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework import serializers
from django.contrib.auth.models import User

# from rest_framework.views import APIView


# from django.core.serializers.json import DjangoJSONEncoder
# from django.db.models.utils import list_to_queryset
# @login_required
@staff_member_required
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
        QuerySETGraficoAgrupado = grafico_ordenado.values('day', 'month', 'year').annotate(CPU_MAX=Max('CPU'), CPU_AVG=Avg('CPU'),CPU_MIN=Min('CPU'),RAM_MAX=Max('RAM'), RAM_AVG=Avg('RAM'),RAM_MIN=Min('RAM'),SWAP_MAX=Max('SWAP'), SWAP_AVG=Avg('SWAP'),SWAP_MIN=Min('SWAP'),DISCO_MAX=Max('disco'), DISCO_AVG=Avg('disco'),DISCO_MIN=Min('disco')).order_by('day', 'month', 'year')

        #QuerySETGraficoAgrupado
        #QuerySETGraficoAgrupado = <QuerySet [(0, 0, 0, 100, 70.2028, 20, 97, 69.4056, 14, 19, 1.5127, 0, 0, 0.0, 0), (6, 12, 2018, 100, 69.1132, 6, 90, 74.7044, 13, 4, 3.0587, 0, 0, 0.0, 0), (7, 12, 2018, 100, 66.2387, 9, 90, 42.739, 12, 1, 0.0785, 0, 0, 0.0, 0), (10, 12, 2018, 100, 69.8956, 6, 87, 70.0566, 13, 4, 0.3221, 0, 0, 0.0, 0), (11, 12, 2018, 100, 66.7481, 25, 98, 84.9292, 22, 96, 30.6317, 0, 5, 4.5411, 0), (12, 12, 2018, 100, 72.514, 6, 95, 75.64, 13, 16, 5.486, 0, 5, 5.0, 5), (13, 12, 2018, 100, 73.5367, 23, 99, 72.0604, 13, 21, 3.308, 0, 5, 5.0, 5)]>
        i=1

        resultList = []

        for row in QuerySETGraficoAgrupado:
                resultList.append(row)

        objectJson = json.dumps(resultList)

        data['gtes'+str(i)] = objectJson
        #data['grafico'] = objectJson
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

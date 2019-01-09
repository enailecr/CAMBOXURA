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
        if not request.user.groups.filter(name='Visualiza relatório').exists():
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
                    tam = len(todos) - 21600

                    grafico = Dashboard.objects.all()[tam:]
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

            return render(request, 'dashboard.html',data)
        return render(request, 'menu.html')

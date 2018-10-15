from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NumeroEntrada
from .forms import NumeroEntradaForm
from django.contrib.auth.decorators import login_required
import re
from django_tables2 import RequestConfig
#from .tables import DispositivoTable

@login_required
def add(request):
    form = NumeroEntradaForm()
    data = {'form' : form}
    return render(request, 'cadastroNumero.html', data)

# @login_required
# def list(request):
#     table = DispositivoTable(Dispositivo.objects.all())
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#     return render(request, 'menu-3d.html', {'table': table})

# @login_required
# def dispositivo_busca(request):
#     dispositivos = Dispositivo.objects.all()
#     filter = request.GET.get('search')
#     if filter:
#         disp = []
#         for dispositivo in dispositivos:
#             if re.search(filter, dispositivo.unidade.sigla, re.IGNORECASE):
#                 disp.append(dispositivo)
#         dispositivos = disp
#     table = DispositivoTable(dispositivos)
#     RequestConfig(request, paginate={'per_page': 10}).configure(table)
#     return render(request, 'menu-3d.html', {'table': table})

@login_required
def numero_novo(request):
    form = NumeroEntradaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/numeros/')

@login_required
def numero_edita(request, id):
    data = {}
    numero = NumeroEntrada.objects.get(id=id)
    form = NumeroEntradaForm(request.POST or None, instance=numero)
    data['numero'] = numero
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/numeros/')
    else:
        return render(request, 'editaNumero.html', data)

@login_required
def numero_remove(request, id):
    numero = NumeroEntrada.objects.get(id=id)
    numero.delete()
    return redirect('/numeros/')

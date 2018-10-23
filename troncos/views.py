from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TroncoSIPForm,TroncoIAXForm,TroncoCustomizadoForm,TroncoForm
from .models import Tronco
import re
from django_tables2 import RequestConfig
from .tables import TroncoTable

#TroncoSIP
@login_required
def addtroncosip(request):
    form = TroncoSIPForm()
    data = {'form' : form}
    return render(request, 'CadastroTroncoSIP.html', data)

#TroncoIAX
@login_required
def addtroncoiax(request):
    form = TroncoIAXForm()
    data = {'form' : form}
    return render(request, 'CadastroTroncoIAX.html', data)

#TroncoCustomizado
@login_required
def addtroncocustomizado(request):
    form = TroncoCustomizadoForm()
    data = {'form' : form}
    return render(request, 'CadastroTroncoCustomizado.html', data)


@login_required
def list(request):
    table = TroncoTable(Tronco.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)
    return render(request, 'troncos.html', {'table': table})

#TroncoSIP
@login_required
def troncosip_novo(request):
    form = TroncoSIPForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/troncos/')

#TroncoIAX
@login_required
def troncoiax_novo(request):
    form = TroncoIAXForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/troncos/')

#TroncoCustomizado
@login_required
def troncocustomizado_novo(request):
    form = TroncoCustomizadoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/troncos/')

@login_required
def tronco_edita(request, id):
    data = {}
    tronco = Tronco.objects.get(id=id)
    form = TroncoForm(request.POST or None, instance=tronco)
    data['tronco'] = tronco
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/troncos/')
    else:
        return render(request, 'editaTronco.html', data)

@login_required
def tronco_remove(request, id):
    tronco = Tronco.objects.get(id=id)
    tronco.delete()
    return redirect('/troncos/')
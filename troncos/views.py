from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import TroncoSIPForm,TroncoIAXForm,TroncoCustomizadoForm

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
    return render(request, 'troncos.html')

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
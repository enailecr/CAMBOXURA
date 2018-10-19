from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FilaForm

@login_required
def add(request):
    form = FilaForm()
    data = {'form' : form}
    return render(request, 'CadastroFila.html', data)

@login_required
def list(request):
    return render(request, 'filas.html')

@login_required
def fila_novo(request):
    form = FilaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/filas/')
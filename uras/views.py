from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UraForm
@login_required
def add(request):
    form = UraForm()
    data = {'form' : form}
    return render(request, 'UraNovo.html', data)

@login_required
def list(request):
    return render(request, 'uras.html')

@login_required
def ura_novo(request):
    form = UraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('/uras/')
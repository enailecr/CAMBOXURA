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
    return render(request, 'dashboard.html',data)

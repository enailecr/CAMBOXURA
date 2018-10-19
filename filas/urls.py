from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add, fila_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'fila-novo/',fila_novo, name='fila_novo'),
]

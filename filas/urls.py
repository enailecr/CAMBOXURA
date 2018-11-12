from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add, fila_novo, fila_edita, fila_remove

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'fila-novo/',fila_novo, name='fila_novo'),
    url(r'fila-edita/(?P<id>\d+)/$', fila_edita, name='fila_edita'),
    url(r'fila-remove/(?P<id>\d+)/$', fila_remove, name='fila_remove'),
]

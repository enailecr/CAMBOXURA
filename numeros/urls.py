from django.urls import path, include
from django.conf.urls import include, url
from .views import list, add, numero_novo, numero_edita, numero_remove, carregaDestinos

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'numero-novo/',numero_novo, name='numero_novo'),
    url(r'numero-edita/(?P<id>\d+)/$', numero_edita, name='numero_edita'),
    url(r'numero-remove/(?P<id>\d+)/$', numero_remove, name='numero_remove'),
]

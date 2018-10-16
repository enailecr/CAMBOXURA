from django.urls import path, include
from django.conf.urls import include, url
from .views import login, add, usuario_novo, usuario_edita

urlpatterns = [
    path(r'add/',add),
    url(r'usuario-novo/',usuario_novo, name='usuario_novo'),
    url(r'usuario-edita/', usuario_edita, name='usuario_edita'),
]

from django.urls import path, include
from django.conf.urls import include, url
from .views import list , busca_relatorios

urlpatterns = [
    path(r'', list),
    url(r'relatorio-busca/',busca_relatorios, name='busca_relatorios'),
]

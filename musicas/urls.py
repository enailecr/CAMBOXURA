from django.urls import path, include
from django.conf.urls import include, url
from .views import list, addcategoria, addstreaming ,streaming_novo, categoria_novo,musica_edita,musica_remove,gravacao_remove, upload_file_cad

urlpatterns = [
    path(r'', list),
    path(r'addcategoria/',addcategoria),
    path(r'addstreaming/',addstreaming),
    url(r'categoria-novo/',categoria_novo, name='categoria_novo'),
    url(r'streaming-novo/',streaming_novo, name='streaming_novo'),
    url(r'musica-edita/(?P<id>\d+)/$', musica_edita, name='musica_edita'),
    url(r'musica-remove/(?P<id>\d+)/$', musica_remove, name='musica_remove'),
    url(r'gravacao-remove/(?P<id>\d+)/$', gravacao_remove, name='gravacao_remove'),
    url(r'musica-novaGravacao/',upload_file_cad, name='gravacao_nova'),
]

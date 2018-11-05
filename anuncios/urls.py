from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add,anuncio_novo,anuncio_edita,anuncio_remove, upload_file_cad,upload_file_edt

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'anuncio-novo/',anuncio_novo, name='anuncio_novo'),
    url(r'anuncio-edita/(?P<id>\d+)/$', anuncio_edita, name='anuncio_edita'),
    url(r'anuncio-remove/(?P<id>\d+)/$', anuncio_remove, name='anuncio_remove'),
    url(r'anuncio-novaGravacao/',upload_file_cad, name='gravacao_nova'),
    url(r'anuncio-editaGravacao/(?P<id>\d+)/$',upload_file_edt, name='gravacao_edita'),
]

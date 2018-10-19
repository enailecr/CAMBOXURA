from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add,anuncio_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'anuncio-novo/',anuncio_novo, name='anuncio_novo'),
]

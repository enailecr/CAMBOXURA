from django.urls import path, include
from django.conf.urls import include, url
from .views import list, addmusica, addstreaming ,streaming_novo, musica_novo

urlpatterns = [
    path(r'', list),
    path(r'addmusica/',addmusica),
    path(r'addstreaming/',addstreaming),
    url(r'musica_novo/',musica_novo, name='musica_novo'),
    url(r'streaming_novo/',streaming_novo, name='streaming_novo'),
]

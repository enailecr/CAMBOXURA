from django.urls import path, include
from django.conf.urls import include, url
from .views import list, add, ura_novo, ura_remove, ura_edita

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'ura-novo/',ura_novo, name='ura_novo'),
    url(r'ura-edita/(?P<id>\d+)/$', ura_edita, name='ura_edita'),
    url(r'ura-remove/(?P<id>\d+)/$', ura_remove, name='ura_remove'),
]

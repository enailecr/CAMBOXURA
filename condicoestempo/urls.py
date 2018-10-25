from django.urls import path, include
from django.conf.urls import include, url

from .views import list ,add , condicoestempo_novo, condicoestempo_edita, condicoestempo_remove

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'condicoestempo-novo/',condicoestempo_novo, name='condicoestempo_novo'),
    url(r'condicoestempo-edita/(?P<id>\d+)/$', condicoestempo_edita, name='condicoestempo_edita'),
    url(r'condicoestempo-remove/(?P<id>\d+)/$', condicoestempo_remove, name='condicoestempo_remove'),
]

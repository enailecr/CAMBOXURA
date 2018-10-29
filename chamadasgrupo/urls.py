from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add, chamadasgrupo_novo ,chamadasgrupo_remove , chamadasgrupo_edita

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'chamadasgrupo-novo/',chamadasgrupo_novo, name='chamadasgrupo_novo'),
    url(r'chamadasgrupo-edita/(?P<id>\d+)/$', chamadasgrupo_edita, name='chamadasgrupo_edita'),
    url(r'chamadasgrupo-remove/(?P<id>\d+)/$', chamadasgrupo_remove, name='chamadasgrupo_remove'),
]

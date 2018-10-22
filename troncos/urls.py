from django.urls import path, include
from django.conf.urls import include, url
from .views import list ,addtroncosip,addtroncoiax,addtroncocustomizado,troncosip_novo,troncoiax_novo,troncocustomizado_novo

urlpatterns = [
    path(r'', list),
    path(r'addtroncosip/',addtroncosip),
    path(r'addtroncoiax/',addtroncoiax),
    path(r'addtroncocustomizado/',addtroncocustomizado),
    url(r'troncosip-novo/',troncosip_novo, name='troncosip_novo'),
    url(r'troncoiax-novo/',troncoiax_novo, name='troncoiax_novo'),
    url(r'troncocustomizado-novo/',troncocustomizado_novo, name='troncocustomizado_novo'),
]

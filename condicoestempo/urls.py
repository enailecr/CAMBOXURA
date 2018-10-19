from django.urls import path, include
from django.conf.urls import include, url

from .views import list ,add , condicoestempo_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'condicoestempo-novo/',condicoestempo_novo, name='condicoestempo_novo'),
]

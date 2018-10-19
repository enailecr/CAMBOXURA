from django.urls import path, include
from django.conf.urls import include, url
from .views import list, add, ura_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'ura-novo/',ura_novo, name='ura_novo'),
]

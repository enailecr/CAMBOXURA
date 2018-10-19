from django.urls import path, include
from django.conf.urls import include, url

from .views import list, add, chamadasgrupo_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'chamadasgrupo-novo/',chamadasgrupo_novo, name='chamadasgrupo_novo'),
]

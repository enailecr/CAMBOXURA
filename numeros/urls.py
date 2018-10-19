from django.urls import path, include
from django.conf.urls import include, url
from .views import list, add , numero_novo

urlpatterns = [
    path(r'', list),
    path(r'add/',add),
    url(r'numero-novo/',numero_novo, name='numero_novo'),
]

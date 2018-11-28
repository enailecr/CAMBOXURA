from django.urls import path, include
from django.conf.urls import include, url

from .views import list, busca_logs, lista_logs_cambox, lista_logs_server, busca_logs_cambox

urlpatterns = [
    path(r'', list),
    url(r'logs-busca/',busca_logs, name='busca_logs'),
    url(r'camboxura/',lista_logs_cambox, name='lista_logs_cambox'),
    url(r'servidor/',lista_logs_server, name='lista_logs_server'),
    url(r'cambox-busca/',busca_logs_cambox, name='busca_logs_cambox'),
]

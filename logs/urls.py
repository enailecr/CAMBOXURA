from django.urls import path, include
from django.conf.urls import include, url

from .views import list, busca_logs

urlpatterns = [
    path(r'', list),
    url(r'logs-busca/',busca_logs, name='busca_logs'),
]

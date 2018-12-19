from django.urls import path, include
from django.conf.urls import include, url
from .views import list , busca_relatorios ,canal_novo, add_canal, lista_canais, canal_remove, canal_edita
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', list),
    url(r'relatorio-busca/',busca_relatorios, name='busca_relatorios'),
    url(r'relatorio-canalnovo/',canal_novo, name='canal_novo'),
    url(r'relatorio-addcanal/',add_canal, name='add_canal'),
    path(r'canais/', lista_canais),
    url(r'canal-remove/(?P<id>\d+)/$', canal_remove, name='canal_remove'),
    url(r'canal-edita/(?P<id>\d+)/$', canal_edita, name='canal_edita'),
]+ static(settings.MEDIA2_URL, document_root=settings.MEDIA2_ROOT)

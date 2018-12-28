from django.urls import path, include
from django.conf.urls import include, url
from .views import list , busca_relatorios ,canal_novo, add_canal, lista_canais, canal_remove, canal_edita, lista_graficos, busca_pizza, busca_linha
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
    path(r'graficos/', lista_graficos),
    url(r'busca-grafico-porcent/',busca_pizza, name='busca_pizza'),
    url(r'busca-grafico-qtd/',busca_linha, name='busca_linha'),
]+ static(settings.MEDIA2_URL, document_root=settings.MEDIA2_ROOT)

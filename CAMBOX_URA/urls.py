from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', home),
    path('admin/', admin.site.urls),
    path(r'contas/', include('django.contrib.auth.urls')),
    path(r'anuncios/', include('anuncios.urls')),
    path(r'chamadasgrupo/', include('chamadasgrupo.urls')),
    path(r'condicoestempo/', include('condicoestempo.urls')),
    path(r'dashboard/', include('dashboard.urls')),
    path(r'filas/', include('filas.urls')),
    path(r'musicas/', include('musicas.urls')),
    path(r'numeros/', include('numeros.urls')),
    path(r'troncos/', include('troncos.urls')),
    path(r'uras/', include('uras.urls')),
    path(r'usuarios/', include('usuarios.urls')),
    path(r'relatorios/', include('relatorios.urls')),
    path(r'logs/', include('logs.urls')),
    path(r'aplicar/', include('aplicar.urls')),
]+ static(settings.MEDIA2_URL, document_root=settings.MEDIA2_ROOT)

from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path(r'', home),
    path('admin/', admin.site.urls),
    path(r'contas/', include('django.contrib.auth.urls')),
    path(r'anuncios/', include('anuncios.urls')),
    path(r'chamadasgrupo/', include('chamadasgrupo.urls')),
    path(r'condicoestempo/', include('condicoestempo.urls')),
    path(r'dashboard/', include('dashboard.urls')),
    path(r'destinos/', include('destinos.urls')),
    path(r'filas/', include('filas.urls')),
    path(r'musicas/', include('musicas.urls')),
    path(r'numeros/', include('numeros.urls')),
    path(r'troncos/', include('troncos.urls')),
    path(r'uras/', include('uras.urls')),
    path(r'usuarios/', include('usuarios.urls')),
    path(r'logs/', include('logs.urls')),
]

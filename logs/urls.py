from django.urls import path, include
from django.conf.urls import include, url

from .views import list

urlpatterns = [
    path(r'', list),
]

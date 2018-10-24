import django_tables2 as tables
#import django_filters
from .models import ChamadaEmGrupo

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class ChamadaEmGrupoTable(tables.Table):
    
    class Meta:
        model = ChamadaEmGrupo
        fields = ('modo', 'descricao','editar','excluir')
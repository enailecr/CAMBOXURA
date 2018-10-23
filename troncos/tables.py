import django_tables2 as tables
#import django_filters
from .models import Tronco

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class TroncoTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/troncos/tronco-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/troncos/tronco-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Tronco
        fields = ('nome', 'callerIDSaida', 'opcoesCID','maxCanais','opcoesDiskAsterisk','contSeOcup','desabTronco','prefixChamSaida','editar','excluir')
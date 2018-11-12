# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import django_tables2 as tables
#import django_filters
from .models import Relatorios

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class RelatoriosTable(tables.Table):
    # excluir = tables.TemplateColumn(
    #         '<form action="/uras/ura-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
    #     orderable=False,
    #     verbose_name=''
    #     )
    # editar = tables.TemplateColumn(
    #         '<form action="/uras/ura-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
    #     orderable=False,
    #     verbose_name=''
    #     )
    class Meta:
        model = Relatorios
        fields = ('data', 'origem','número de Destino','canal Origem','canal de Destino','ação da URA','código de Contuta', 'status', 'duração','áudio')

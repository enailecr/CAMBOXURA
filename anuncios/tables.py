import django_tables2 as tables
#import django_filters
from .models import Anuncio

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class AnuncioTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/anuncios/anuncio-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/anuncios/anuncio-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip" title="Please note that deletion cannot be undone" type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Anuncio
        fields = ( 'descricao','editar','excluir')
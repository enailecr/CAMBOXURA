# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import django_tables2 as tables
#import django_filters
from .models import Cdr, Canal

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class RelatoriosTable(tables.Table):

    detalhes = tables.TemplateColumn(
            '<button data-toggle="tooltip" onClick="mostraDetalhes(\'{{record.calldate}}\',\'{{record.clid}}\''
            +',\'{{record.src}}\',\'{{record.dst}}\',\'{{record.dcontext}}\',\'{{record.channel}}\',\'{{record.dstchannel}}\''
            +',\'{{record.lastapp}}\',\'{{record.lastdata}}\',\'{{record.duration}}\',\'{{record.billsec}}\',\'{{record.disposition}}\''
            +',\'{{record.amaflags}}\',\'{{record.accountcode}}\',\'{{record.userfield}}\',\'{{record.recordingfile}}\',\'{{record.cnum}}\''
            +',\'{{record.cnam}}\',\'{{record.outbound_cnum}}\',\'{{record.outbound_cnam}}\',\'{{record.dst_cnam}}\',\'{{record.did}}\');"'
            +'  type="button" class="btn btn-danger btn-xs">Detalhes</button>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Cdr
        fields = ('calldate', 'src','dst','channel','dstchannel','duration','accountcode', 'disposition', 'detalhes')

class CanaisTable(tables.Table):
    excluir = tables.TemplateColumn(
            '<form action="/relatorios/canal-remove/{{record.id}}/" method="post">{% csrf_token %}<input type="hidden" name="_method" value="Excluir"><button data-toggle="tooltip" title="Exclusão não pode ser desfeita" type="submit" class="btn btn-danger btn-xs">Excluir</button></form>',
        orderable=False,
        verbose_name=''
        )
    editar = tables.TemplateColumn(
            '<form action="/relatorios/canal-edita/{{record.id}}/" method="get">{% csrf_token %}<input type="hidden" name="_method" value="Editar"><button data-toggle="tooltip"  type="submit" class="btn btn-danger btn-xs">Editar</button></form>',
        orderable=False,
        verbose_name=''
        )
    class Meta:
        model = Canal
        fields = ('nome','editar','excluir')

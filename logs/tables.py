import django_tables2 as tables
#import django_filters
from .models import Log, LogCambox

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class LogsTable(tables.Table):
    class Meta:
        model = Log
        fields = ( 'data','log')

class LogsCamboxTable(tables.Table):
    data = tables.Column()
    tipo = tables.Column()
    processo = tables.Column()
    chamada = tables.Column()
    log = tables.Column()

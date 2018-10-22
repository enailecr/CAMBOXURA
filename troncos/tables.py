import django_tables2 as tables
#import django_filters
from .models import Tronco

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class TroncoTable(tables.Table):

    class Meta:
        model = Tronco
        fields = ('nome', 'callerIDSaida', 'opcoesCID','maxCanais','opcoesDiskAsterisk','contSeOcup','desabTronco','prefixChamSaida')
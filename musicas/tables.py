import django_tables2 as tables
#import django_filters
from .models import Musica

from django.db import models
from django.utils import six
from django.utils.html import escape, format_html

from django_tables2.utils import AttributeDict, ucfirst

class MusicaTable(tables.Table):

    class Meta:
        model = Musica
        fields = ('nome','teste')
from django.forms import ModelForm
from .models import Log

class LogsForm(ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

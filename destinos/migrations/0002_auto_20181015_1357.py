# Generated by Django 2.1.2 on 2018-10-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='tipo',
            field=models.CharField(choices=[('1', 'Anúncio'), ('2', 'Gravação'), ('3', 'Número de entrada'), ('4', 'URA'), ('5', 'Fila'), ('6', 'Chamada em grupo'), ('7', 'Condições de tempo'), ('8', 'Tronco')], max_length=1),
        ),
    ]
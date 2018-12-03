# Generated by Django 2.1.1 on 2018-12-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumeroEntrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Anúncio'), ('2', 'Gravação'), ('3', 'Número de entrada'), ('4', 'URA'), ('5', 'Fila'), ('6', 'Chamada em grupo'), ('7', 'Condições de tempo'), ('8', 'Tronco')], max_length=1)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('origem', models.IntegerField()),
                ('atendido', models.BooleanField()),
                ('gravaChamada', models.BooleanField()),
                ('destino', models.IntegerField(blank=True, null=True)),
                ('destinoTipo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

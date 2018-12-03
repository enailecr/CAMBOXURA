# Generated by Django 2.1.1 on 2018-12-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcaoURA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.IntegerField(blank=True, null=True)),
                ('tipoDestino', models.IntegerField(blank=True, null=True)),
                ('ramal', models.CharField(blank=True, max_length=10, null=True)),
                ('retornar', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='URA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Anúncio'), ('2', 'Gravação'), ('3', 'Número de entrada'), ('4', 'URA'), ('5', 'Fila'), ('6', 'Chamada em grupo'), ('7', 'Condições de tempo'), ('8', 'Tronco')], max_length=1)),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=100)),
                ('discarDireto', models.CharField(choices=[('0', 'Desabilitado'), ('1', 'Ramais')], max_length=1)),
                ('timeout', models.IntegerField()),
                ('tentativasInvalidas', models.IntegerField(blank=True, null=True)),
                ('anexAnuncInvalid', models.BooleanField()),
                ('returnInvalid', models.BooleanField()),
                ('destinoInvalid', models.IntegerField(blank=True, null=True)),
                ('destinoInvalidTipo', models.CharField(blank=True, max_length=1, null=True)),
                ('retentativasTimeout', models.IntegerField(blank=True, null=True)),
                ('anexAnuncTimeout', models.BooleanField()),
                ('retornarTimeout', models.BooleanField()),
                ('destinoTimeout', models.IntegerField(blank=True, null=True)),
                ('destinoTimeoutTipo', models.CharField(blank=True, max_length=1, null=True)),
                ('returnURACaixaPostal', models.BooleanField()),
                ('anuncioUra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anuncios.Anuncio')),
                ('gravInvalid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gravInvalidURA', to='anuncios.Gravacao')),
                ('gravRepetInvalid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anuncios.Gravacao')),
                ('gravRetentTimeout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gravRepetInvalidURA', to='anuncios.Gravacao')),
                ('gravTimeout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gravTimeoutURA', to='anuncios.Gravacao')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='opcaoura',
            name='ura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uras.URA'),
        ),
    ]

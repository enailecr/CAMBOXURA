# Generated by Django 2.1.1 on 2018-12-03 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Anúncio'), ('2', 'Gravação'), ('3', 'Número de entrada'), ('4', 'URA'), ('5', 'Fila'), ('6', 'Chamada em grupo'), ('7', 'Condições de tempo'), ('8', 'Tronco')], max_length=1)),
                ('descricao', models.CharField(max_length=50)),
                ('repeticao', models.CharField(blank=True, max_length=1, null=True)),
                ('pula', models.BooleanField()),
                ('retornaURA', models.BooleanField()),
                ('canalNaoResp', models.BooleanField()),
                ('destino', models.IntegerField(blank=True, null=True)),
                ('destinoTipo', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gravacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('1', 'Anúncio'), ('2', 'Gravação'), ('3', 'Número de entrada'), ('4', 'URA'), ('5', 'Fila'), ('6', 'Chamada em grupo'), ('7', 'Condições de tempo'), ('8', 'Tronco')], max_length=1)),
                ('nome', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=255)),
                ('musica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicas.MusicaCategoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='anuncio',
            name='gravacaoAn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncios.Gravacao'),
        ),
    ]

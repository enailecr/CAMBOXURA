# Generated by Django 2.1.2 on 2018-11-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicacategoria',
            name='volume',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]

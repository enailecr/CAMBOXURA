# Generated by Django 2.1.1 on 2018-11-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filas', '0005_auto_20181113_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentesdinamicos',
            name='numero',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='membrosdinamicos',
            name='numero',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
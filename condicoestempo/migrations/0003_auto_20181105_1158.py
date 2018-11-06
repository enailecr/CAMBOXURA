# Generated by Django 2.1.2 on 2018-11-05 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condicoestempo', '0002_grupotempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupotempo',
            name='condTempo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='condicoestempo.CondicaoTempo'),
        ),
        migrations.AlterField(
            model_name='grupotempo',
            name='diaSemanaFim',
            field=models.CharField(choices=[('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=13),
        ),
        migrations.AlterField(
            model_name='grupotempo',
            name='diaSemanaInicio',
            field=models.CharField(choices=[('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=13),
        ),
    ]

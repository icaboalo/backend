# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0003_auto_20160220_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vuelo',
            name='destino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destino.Destino'),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vuelo',
            name='hora',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
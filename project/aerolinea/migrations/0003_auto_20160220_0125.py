# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 01:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aerolinea', '0002_auto_20160220_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aerolinea',
            options={'verbose_name': 'Aerolinea', 'verbose_name_plural': 'Aerolineas'},
        ),
        migrations.AlterModelOptions(
            name='bitacora',
            options={'verbose_name': 'Bitacora', 'verbose_name_plural': 'Bitacoras'},
        ),
        migrations.AlterModelOptions(
            name='vuelo',
            options={'verbose_name': 'Vuelo', 'verbose_name_plural': 'Vuelos'},
        ),
    ]

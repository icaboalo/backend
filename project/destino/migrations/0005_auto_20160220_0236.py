# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 02:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destino', '0004_auto_20160220_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='pais',
            field=models.CharField(choices=[('EU', 'ESTADOS UNIDOS'), ('MX', 'MEXICO'), ('AU', 'AUSTRALIA'), ('FR', 'FRANCIA'), ('BR', 'BRASIL'), ('SA', 'SUDAFRICA'), ('SP', 'ESPAÑA')], max_length=2),
        ),
        migrations.AlterField(
            model_name='destino',
            name='rating',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]

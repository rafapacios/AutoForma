# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-11 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodcad',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]

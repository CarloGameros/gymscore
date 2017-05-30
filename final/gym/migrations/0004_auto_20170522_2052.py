# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-22 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_auto_20170521_0454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='Peso',
            new_name='Pesoi',
        ),
        migrations.AddField(
            model_name='usuario',
            name='Pesoa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='avance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True),
        ),
    ]

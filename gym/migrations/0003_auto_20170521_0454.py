# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_usuario_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sex',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('I', 'Indistinto')], default='I', max_length=1),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], default='U', max_length=1),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('editorial', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=1000, null=True)),
            ],
        ),
    ]
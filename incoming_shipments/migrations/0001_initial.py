# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_no', models.CharField(max_length=8, verbose_name='SHIP NO')),
                ('supplier', models.CharField(max_length=30, verbose_name='Supplier')),
                ('Port_ETA', models.DateTimeField(verbose_name='ETA date')),
                ('Store_ETA', models.DateTimeField(verbose_name='Into Store date')),
                ('Comment', models.CharField(max_length=30, verbose_name='Comment')),
            ],
        ),
    ]

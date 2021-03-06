# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_requests', '0005_request_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='OTP',
            field=models.CharField(choices=[('AIR', 'AIR'), ('SEA', 'SEA'), ('LOC', 'LOC')], default='AIR', max_length=3, verbose_name='Order Type'),
        ),
        migrations.AlterField(
            model_name='request',
            name='WH',
            field=models.CharField(choices=[('SVI', 'SVI'), ('SQL', 'SQL'), ('SNW', 'SNW'), ('SWA', 'SWA')], default='SVI', max_length=3),
        ),
    ]

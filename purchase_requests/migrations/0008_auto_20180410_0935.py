# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-09 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_requests', '0007_remove_request_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='OTP',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='request',
            name='WH',
            field=models.CharField(max_length=3),
        ),
    ]

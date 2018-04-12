# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-10 00:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_requests', '0010_auto_20180410_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
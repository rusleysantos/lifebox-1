# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 16:45
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20171109_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='createdPor',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=10, verbose_name='auth.user'),
        ),
    ]
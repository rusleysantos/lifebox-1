# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171109_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='createdPor',
            field=models.ForeignKey(default='auth.user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

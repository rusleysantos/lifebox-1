# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20171025_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='viagem',
            name='status',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='status', to='core.Status'),
        ),
    ]

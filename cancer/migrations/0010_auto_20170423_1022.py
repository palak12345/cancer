# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0009_auto_20170422_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cancer.Access'),
        ),
    ]

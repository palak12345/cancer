# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0010_auto_20170423_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_title',
            field=models.CharField(max_length=1000),
        ),
    ]

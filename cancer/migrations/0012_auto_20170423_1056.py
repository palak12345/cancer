# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-23 10:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0011_auto_20170423_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='user',
            new_name='access',
        ),
        migrations.AlterField(
            model_name='access',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0002_home'),
    ]

    operations = [
        migrations.DeleteModel(
            name='home',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.FileField(upload_to=''),
        ),
    ]

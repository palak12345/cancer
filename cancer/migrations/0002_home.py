# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=250)),
                ('login', models.CharField(max_length=500)),
            ],
        ),
    ]

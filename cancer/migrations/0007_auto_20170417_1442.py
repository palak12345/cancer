# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 14:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cancer', '0006_auto_20170414_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cancer_type', models.CharField(max_length=250)),
                ('blood_group', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=500)),
                ('cancer_logo', models.FileField(max_length=2000, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='query',
            name='query_title',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='query',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cancer.Access'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='access',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

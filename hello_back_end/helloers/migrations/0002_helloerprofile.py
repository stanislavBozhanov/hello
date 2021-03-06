# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelloerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_id', models.SmallIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.SmallIntegerField()),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=100)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloers', '0002_helloerprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HelloerProfile',
            new_name='Helloer',
        ),
    ]
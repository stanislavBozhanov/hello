# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloers', '0004_friends'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friends',
            new_name='Friendship',
        ),
        migrations.RenameField(
            model_name='friendship',
            old_name='friend_id',
            new_name='friend',
        ),
        migrations.RenameField(
            model_name='friendship',
            old_name='user_id',
            new_name='user',
        ),
    ]

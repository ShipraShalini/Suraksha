# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 22:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170414_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='position',
            new_name='location',
        ),
    ]

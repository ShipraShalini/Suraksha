# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20170414_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='desc',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
    ]
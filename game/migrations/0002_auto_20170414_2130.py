# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='desc',
        ),
        migrations.AlterField(
            model_name='subject',
            name='desc',
            field=models.TextField(),
        ),
    ]
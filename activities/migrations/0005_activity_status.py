# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_enviroment'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headquarters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headquarters',
            name='status',
            field=models.DateTimeField(null=True),
        ),
    ]

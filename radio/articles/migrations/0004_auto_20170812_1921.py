# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-12 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170811_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_program_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='program',
            name='slug',
            field=models.SlugField(default=1, editable=False),
            preserve_default=False,
        ),
    ]
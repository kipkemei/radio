# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0003_auto_20170730_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='day',
            new_name='name',
        ),
    ]
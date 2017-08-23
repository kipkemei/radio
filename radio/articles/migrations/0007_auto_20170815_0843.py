# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-15 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20170814_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('name', 'article')]),
        ),
        migrations.AlterIndexTogether(
            name='tag',
            index_together=set([('name', 'article')]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20160509_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='category',
            new_name='categories',
        ),
    ]
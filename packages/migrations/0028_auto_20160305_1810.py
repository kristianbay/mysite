# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 17:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0027_auto_20160303_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['shortname']},
        ),
    ]
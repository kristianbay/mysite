# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0020_auto_20160302_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_number',
            field=models.CharField(default='', max_length=40),
        ),
    ]

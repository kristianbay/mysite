# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-03 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0024_auto_20160303_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='inv_customer_id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='customerproduct',
            old_name='inv_production_order_id',
            new_name='production_order_id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='inv_product_id',
            new_name='product_id',
        ),
    ]

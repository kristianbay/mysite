# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0019_auto_20160301_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='update_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='customerproduct',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='package',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='package',
            name='update_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='packageversion',
            name='release_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date released'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='productpackage',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='date created'),
        ),
    ]

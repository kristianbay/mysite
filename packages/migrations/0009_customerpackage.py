# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0008_customeruser_create_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Customer')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Package')),
            ],
        ),
    ]

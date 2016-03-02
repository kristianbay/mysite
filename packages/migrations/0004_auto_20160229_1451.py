# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20160130_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created')),
                ('update_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date updated')),
            ],
        ),
        migrations.CreateModel(
            name='PackageVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=40)),
                ('release_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date released')),
                ('changelog', models.CharField(default='', max_length=255)),
                ('path', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='package',
            name='changelog',
        ),
        migrations.RemoveField(
            model_name='package',
            name='path',
        ),
        migrations.RemoveField(
            model_name='package',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='version',
        ),
        migrations.AddField(
            model_name='package',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='package',
            name='update_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='packageversion',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.Package'),
        ),
    ]

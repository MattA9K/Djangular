# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='coordinates_lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='region',
            name='coordinates_long',
            field=models.FloatField(),
        ),
    ]
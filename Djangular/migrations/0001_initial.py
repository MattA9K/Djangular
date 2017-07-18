# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangularCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('code', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DjangularDirective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled Djangular Directive', help_text='Cosmetic display name for this directive in the primary navigation view', max_length=55)),
                ('directive_js', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangularIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('code', models.CharField(max_length=75, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DjangularMasterViewController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled Djangular Application', help_text='Cosmetic display name for this app in the primary navigation view', max_length=55)),
                ('module_js', models.TextField()),
                ('controller_js', models.TextField()),
                ('view_html', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Djangular.DjangularCategory')),
                ('djangular_directive', models.ManyToManyField(to='Djangular.DjangularDirective')),
            ],
        ),
        migrations.CreateModel(
            name='DjangularService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled Djangular Service', help_text='Cosmetic display name for this service in the primary navigation view', max_length=55)),
                ('service_js', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangularSlaveViewController',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('title', models.CharField(default='Untitled Djangular Directive', help_text='Cosmetic display name for this directive in the primary navigation view', max_length=55)),
                ('controller_js', models.TextField()),
                ('view_html', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='djangularmasterviewcontroller',
            name='djangular_service',
            field=models.ManyToManyField(to='Djangular.DjangularService'),
        ),
        migrations.AddField(
            model_name='djangularmasterviewcontroller',
            name='djangular_slave_vc',
            field=models.ManyToManyField(to='Djangular.DjangularSlaveViewController'),
        ),
        migrations.AddField(
            model_name='djangularmasterviewcontroller',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Djangular.DjangularIcon'),
        ),
    ]

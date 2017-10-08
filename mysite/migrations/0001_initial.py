# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=200, unique=True)),
                ('app_name', models.CharField(max_length=200)),
                ('developer_name', models.CharField(max_length=200)),
                ('developer_email', models.CharField(max_length=200)),
                ('icon_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200, unique=True)),
                ('count', models.IntegerField(default=0)),
                ('results', models.ManyToManyField(to='mysite.Result')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=20)),
                ('process', models.CharField(max_length=20)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='mobile',
            field=models.CharField(max_length=11, unique=True, verbose_name='\u7535\u8bdd'),
        ),
    ]

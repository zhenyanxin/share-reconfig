# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-21 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180421_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, verbose_name='\u5bc6\u7801'),
        ),
    ]

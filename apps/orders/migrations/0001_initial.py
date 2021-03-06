# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-21 11:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentOrder',
            fields=[
                ('order_id', models.CharField(default='3123', max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('payer_acount', models.CharField(max_length=100, verbose_name='\u652f\u4ed8\u8d26\u6237')),
                ('payee_acount', models.CharField(max_length=100, verbose_name='\u6536\u6b3e\u8d26\u6237')),
                ('pay_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('payment_method', models.CharField(choices=[('\u5fae\u4fe1', '\u5fae\u4fe1'), ('\u652f\u4ed8\u5b9d', '\u652f\u4ed8\u5b9d'), ('\u7f51\u94f6', '\u7f51\u94f6')], default=('\u5fae\u4fe1', '\u5fae\u4fe1'), max_length=50, verbose_name='\u652f\u4ed8\u65b9\u5f0f')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u79df\u8d41\u91d1\u989d')),
                ('damages', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u8d54\u507f\u91d1\u989d')),
                ('poundage', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5e73\u53f0\u6263\u9664')),
                ('receipt', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5b9e\u9645\u5230\u8d26')),
                ('note', models.TextField(default='', max_length=200, verbose_name='\u7559\u8a00')),
                ('comment', models.TextField(default='', max_length=200, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u8ba2\u5355',
                'verbose_name_plural': '\u8bbe\u5907\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='SoftwareOrder',
            fields=[
                ('order_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('payer_acount', models.CharField(max_length=100, verbose_name='\u652f\u4ed8\u8d26\u6237')),
                ('payee_acount', models.CharField(max_length=100, verbose_name='\u6536\u6b3e\u8d26\u6237')),
                ('pay_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('payment_method', models.CharField(choices=[('\u5fae\u4fe1', '\u5fae\u4fe1'), ('\u652f\u4ed8\u5b9d', '\u652f\u4ed8\u5b9d'), ('\u7f51\u94f6', '\u7f51\u94f6')], default=('\u5fae\u4fe1', '\u5fae\u4fe1'), max_length=50, verbose_name='\u652f\u4ed8\u65b9\u5f0f')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u79df\u8d41\u91d1\u989d')),
                ('damages', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u8d54\u507f\u91d1\u989d')),
                ('poundage', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5e73\u53f0\u6263\u9664')),
                ('receipt', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5b9e\u9645\u5230\u8d26')),
                ('note', models.TextField(default='', max_length=200, verbose_name='\u7559\u8a00')),
                ('comment', models.TextField(default='', max_length=200, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8f6f\u4ef6\u8ba2\u5355',
                'verbose_name_plural': '\u8f6f\u4ef6\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='TechnologyOrder',
            fields=[
                ('order_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='\u8ba2\u5355\u53f7')),
                ('payer_acount', models.CharField(max_length=100, verbose_name='\u652f\u4ed8\u8d26\u6237')),
                ('payee_acount', models.CharField(max_length=100, verbose_name='\u6536\u6b3e\u8d26\u6237')),
                ('pay_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
                ('payment_method', models.CharField(choices=[('\u5fae\u4fe1', '\u5fae\u4fe1'), ('\u652f\u4ed8\u5b9d', '\u652f\u4ed8\u5b9d'), ('\u7f51\u94f6', '\u7f51\u94f6')], default=('\u5fae\u4fe1', '\u5fae\u4fe1'), max_length=50, verbose_name='\u652f\u4ed8\u65b9\u5f0f')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u79df\u8d41\u91d1\u989d')),
                ('damages', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u8d54\u507f\u91d1\u989d')),
                ('poundage', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5e73\u53f0\u6263\u9664')),
                ('receipt', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='\u5b9e\u9645\u5230\u8d26')),
                ('note', models.TextField(default='', max_length=200, verbose_name='\u7559\u8a00')),
                ('comment', models.TextField(default='', max_length=200, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u6280\u672f\u8ba2\u5355',
                'verbose_name_plural': '\u6280\u672f\u8ba2\u5355',
            },
        ),
    ]

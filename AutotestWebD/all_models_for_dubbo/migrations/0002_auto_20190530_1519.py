# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-30 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_models_for_dubbo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb2dubbointerface',
            name='customUri',
            field=models.CharField(db_column='customUri', default='', max_length=200, verbose_name='自定义请求地址'),
        ),
        migrations.AddField(
            model_name='tb2dubbointerface',
            name='useCustomUri',
            field=models.IntegerField(db_column='useCustomUri', default=0, verbose_name='是否使用自定义请求地址'),
        ),
        migrations.AddField(
            model_name='tb2dubbotestcasestep',
            name='customUri',
            field=models.CharField(db_column='customUri', default='', max_length=200, verbose_name='自定义请求地址'),
        ),
        migrations.AddField(
            model_name='tb2dubbotestcasestep',
            name='useCustomUri',
            field=models.IntegerField(db_column='useCustomUri', default=0, verbose_name='是否使用自定义请求地址'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
    ]

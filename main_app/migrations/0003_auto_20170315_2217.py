# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20170310_0430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='podrob',
            new_name='site',
        ),
        migrations.AddField(
            model_name='news',
            name='number_news',
            field=models.PositiveIntegerField(default=1, verbose_name='Номер_новости'),
            preserve_default=False,
        ),
    ]

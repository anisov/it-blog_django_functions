# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0003_auto_20170315_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Full_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_all1', models.TextField(verbose_name='Новость полностью')),
                ('number_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.News', verbose_name='Номер_новости')),
            ],
        ),
    ]

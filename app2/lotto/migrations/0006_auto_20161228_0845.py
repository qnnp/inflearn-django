# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto', '0005_guessnumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guessnumbers',
            name='lottos',
            field=models.CharField(default='[1,2,3,4,5,6]', max_length=255),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ip2app', '0005_auto_20190306_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizobject',
            name='url_slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

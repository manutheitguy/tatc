# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='Emmanuel Makonde', max_length=100),
        ),
    ]

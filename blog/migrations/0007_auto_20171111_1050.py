# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171111_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='static/blog/images/'),
        ),
    ]

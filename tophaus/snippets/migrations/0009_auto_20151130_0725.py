# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_auto_20151130_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='number_of_roommates',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

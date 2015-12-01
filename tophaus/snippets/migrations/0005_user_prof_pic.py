# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_auto_20151123_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prof_pic',
            field=models.CharField(default='sample', max_length=200),
            preserve_default=False,
        ),
    ]

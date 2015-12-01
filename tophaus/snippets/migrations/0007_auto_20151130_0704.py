# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20151130_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b''),
        ),
    ]

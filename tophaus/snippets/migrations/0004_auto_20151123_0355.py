# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_amenity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0009_auto_20151130_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='length_of_stay',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='preferences',
            field=multiselectfield.db.fields.MultiSelectField(max_length=35, choices=[(b'Gym', b'Gym'), (b'Full Kitchen', b'Full Kitchen'), (b'TV', b'TV'), (b'Internet Access', b'Internet Access')]),
        ),
    ]

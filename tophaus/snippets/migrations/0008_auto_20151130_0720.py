# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0007_auto_20151130_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='style',
            field=models.CharField(max_length=25, choices=[(b'Convertible', b'Convertible'), (b'Studio', b'Studio'), (b'Convertible Studio', b'Convertible Studio'), (b'Alcove Studio', b'Alcove Studio'), (b'Loft', b'Loft'), (b'Junior 1-bedroom', b'Junior 1-bedroom'), (b'Junior 4', b'Junior 4'), (b'Three-Room', b'Three-Room'), (b'Two-Bedroom', b'Two-Bedroom'), (b'Wing Two-Bedroom', b'Wing Two-Bedroom'), (b'Classic Six', b'Classic Six'), (b'Duplex or Triplex', b'Duplex or Triplex'), (b'Garden Apartment', b'Garden Apartment')]),
        ),
    ]

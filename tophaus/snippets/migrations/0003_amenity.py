# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=255)),
                ('schools', models.CharField(max_length=255)),
                ('garden_backyard', models.CharField(max_length=3)),
                ('pool', models.CharField(max_length=3)),
                ('gym', models.CharField(max_length=3)),
                ('shopping_mall', models.CharField(max_length=255)),
                ('houses', models.ManyToManyField(to='snippets.House')),
            ],
        ),
    ]

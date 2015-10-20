# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=20)),
                ('budget', models.IntegerField(default=0)),
                ('number_of_roommates', models.IntegerField(default=0)),
                ('style', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=400)),
                ('type_of_time', models.CharField(max_length=1, choices=[(b'D', b'Day'), (b'M', b'Month'), (b'Y', b'Year')])),
                ('length_of_stay', models.IntegerField()),
                ('preferences', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=40)),
            ],
        ),
    ]

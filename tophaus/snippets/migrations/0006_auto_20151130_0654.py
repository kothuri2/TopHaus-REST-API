# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_user_prof_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='prof_pic',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(default='null', upload_to=b''),
            preserve_default=False,
        ),
    ]

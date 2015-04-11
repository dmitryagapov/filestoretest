# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_links',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

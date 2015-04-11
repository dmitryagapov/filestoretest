# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import file.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.FileField(upload_to=file.models.file_name)),
            ],
            options={
                'db_table': 'file',
            },
            bases=(models.Model,),
        ),
    ]

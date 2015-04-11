# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20150404_1649'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='myuser',
            table='my_user',
        ),
    ]

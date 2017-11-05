# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170919_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='cover',
            field=models.ImageField(default=datetime.datetime(2017, 11, 5, 3, 46, 33, 296291, tzinfo=utc), upload_to=b'covers/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]

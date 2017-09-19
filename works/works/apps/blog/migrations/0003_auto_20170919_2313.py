# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='context',
            new_name='content',
        ),
    ]

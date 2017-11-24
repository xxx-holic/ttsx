# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(),
        ),
    ]

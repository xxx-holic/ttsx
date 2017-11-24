# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_user', '0001_initial'),
        ('tt_goods', '0002_auto_20171111_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nums', models.IntegerField()),
                ('goods', models.ForeignKey(to='tt_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='ttsx_user.UserInfo')),
            ],
        ),
    ]

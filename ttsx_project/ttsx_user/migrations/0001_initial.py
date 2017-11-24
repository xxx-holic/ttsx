# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sjr', models.CharField(max_length=20)),
                ('sjh', models.CharField(max_length=11)),
                ('addr', models.CharField(max_length=100)),
                ('isDelete', models.BooleanField(default=False)),
                ('sheng', models.IntegerField()),
                ('shi', models.IntegerField()),
                ('qu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(null=True, to='ttsx_user.AreaInfo', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=30)),
                ('isActive', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='user',
            field=models.ForeignKey(to='ttsx_user.UserInfo'),
        ),
    ]

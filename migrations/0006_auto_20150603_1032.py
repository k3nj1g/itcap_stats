# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20150603_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='org',
            field=models.OneToOneField(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='itcap.Organization'),
            preserve_default=True,
        ),
    ]

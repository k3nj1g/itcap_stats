# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20150601_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='org_group',
        ),
        migrations.AddField(
            model_name='org',
            name='stat_all',
            field=models.ManyToManyField(related_name='statistic', null=True, verbose_name='\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430', to='stats.Stats', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='orggroup',
            name='orgs',
            field=models.ManyToManyField(related_name='stat_org', verbose_name='\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439', to='stats.Org'),
            preserve_default=True,
        ),
    ]

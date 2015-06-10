# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20150603_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='itcap.Organization'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='org',
            name='stat_all',
            field=models.ManyToManyField(related_name='statistics', null=True, verbose_name='\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430', to='stats.Stats', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stats',
            name='user_changed',
            field=models.ForeignKey(related_name='user_changed', verbose_name='\u0418\u0437\u043c\u0435\u043d\u0438\u043b', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]

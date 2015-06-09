# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orggroup',
            options={'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438', 'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u0430 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='orggroup',
            name='description',
            field=models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
            preserve_default=True,
        ),
    ]

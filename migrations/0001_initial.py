# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('itcap', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org', models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='itcap.Organization')),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrgGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u0440\u0443\u043f\u043f\u044b')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period', models.DateField(verbose_name='\u041f\u0435\u0440\u0438\u043e\u0434 \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438')),
                ('calls', models.PositiveIntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0439')),
                ('requests', models.PositiveIntegerField(verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u043f\u0440\u043e\u0441\u043e\u0432')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e')),
                ('user_changed', models.ForeignKey(related_name='user_changed', verbose_name='\u0418\u0437\u043c\u0435\u043d\u0438\u043b', to=settings.AUTH_USER_MODEL)),
                ('user_created', models.ForeignKey(related_name='user_created', verbose_name='\u0421\u043e\u0437\u0434\u0430\u043b', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0430 \u043c\u0435\u0441\u044f\u0446',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0430 \u043c\u0435\u0441\u044f\u0446',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='org',
            name='org_group',
            field=models.ForeignKey(related_name='org_group', verbose_name='\u0413\u0440\u0443\u043f\u043f\u0430 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439', to='stats.OrgGroup'),
            preserve_default=True,
        ),
    ]

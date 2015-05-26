# -*- coding: utf-8 -*-
from django.db import models
import datetime

from django.contrib.auth.models import User
from itcap.models import Organization


class OrgGroup(models.Model):
    name = models.CharField(u'Наименование группы', max_length=500)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Статистика'
        verbose_name = u'Статистика'


class Org(models.Model):
    org = models.ForeignKey(Organization, verbose_name=u'Организация')
    org_group = models.ForeignKey(OrgGroup, related_name='org_group', verbose_name=u'Группа организаций')

    class Meta:
        verbose_name_plural = u'Статистика организации'
        verbose_name = u'Статистика организации'


class Stats(models.Model):
    period = models.DateField()
    calls = models.PositiveIntegerField(u'Количество обращений')
    requests = models.PositiveIntegerField(u'Количество запросов')
    date_create = models.DateTimeField(u'Дата создания', default=datetime.datetime.now)
    user_create = models.ForeignKey(User, verbose_name=u'Создал')
    date_change = models.DateTimeField(u'Дата изменения', default=datetime.datetime.now)
    user_change = models.ForeignKey(User, verbose_name=u'Изменил')

    class Meta:
        verbose_name_plural = u'Статистика за месяц'
        verbose_name = u'Статистика за месяц'
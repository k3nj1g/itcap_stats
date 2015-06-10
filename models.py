# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from itcap.models import Organization


class Org(models.Model):
    org = models.ForeignKey(Organization, verbose_name=u'Организация')
    stat_all = models.ManyToManyField('Stats', verbose_name=u'Статистика', related_name='statistics', blank=True,
                                      null=True)

    def __unicode__(self):
        return self.org.name

    class Meta:
        verbose_name_plural = u'Статистика организации'
        verbose_name = u'Статистика организации'

    def get_sum(self):
        st_sum = 0
        for month in self.stat_all.all():
            st_sum += month.sum_all
        return st_sum


class OrgGroup(models.Model):
    name = models.CharField(u'Наименование группы', max_length=500)
    description = models.TextField(u'Описание')
    orgs = models.ManyToManyField('Org', verbose_name=u'Статистика организаций', related_name='stat_org')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Группа статистики'
        verbose_name = u'Группа статистики'


class Stats(models.Model):
    period = models.DateField(u'Период статистики')
    calls = models.PositiveIntegerField(u'Количество обращений')
    requests = models.PositiveIntegerField(u'Количество запросов')
    created = models.DateTimeField(u'Создано', auto_now_add=True)
    modified = models.DateTimeField(u'Изменено', auto_now=True)
    user_created = models.ForeignKey(User, verbose_name=u'Создал', related_name='user_created')
    user_changed = models.ForeignKey(User, verbose_name=u'Изменил', related_name='user_changed', null=True, blank=True)

    def __unicode__(self):
        return str(self.period)

    class Meta:
        verbose_name_plural = u'Статистика за месяц'
        verbose_name = u'Статистика за месяц'

        permissions = (
            ("edit_stats", u"Может редактировать статистику"),
        )
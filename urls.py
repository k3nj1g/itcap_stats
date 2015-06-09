from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
                       url(r'^$', stats_group, name='stats_group'),
                       url(r'^group/(?P<id>\d+)/$', stats_orgs, name='stats_orgs'),
                       url(r'^add_st/(?P<id>\d+)/$', add_stats_page, name='add_stats_page'),
                       url(r'^add_stat/$', add_stat, name='add_stat'),
                       url(r'^org/(?P<id>\d+)/$', stats_org, name='stats_org'),
                       url(r'^get_stat', get_stat),
)
from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
                       url(r'^$', stats_group, name='stats_group'),
                       url(r'^group/(?P<id>\d+)/$', stats_orgs, name='stats_orgs'),
                       url(r'^org/(?P<id>\d+)/$', stats_org, name='stats_org'),
                       url(r'^get_stat', get_stat),
                       url(r'^chart/(?P<id>\d+)/$', requests_chart_view, name='chart'),
)
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import json

from .forms import *
from .models import *


@permission_required('edit_stats')
def stats_group(request):
    st_group = OrgGroup.objects.all()
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            st_group = form.save()
            st_group.save()
            return HttpResponseRedirect('/stats/')
    else:
        form = NewGroupForm()
    return render_to_response('st_gr.html', {'st_group': st_group, 'form': form},
                              context_instance=RequestContext(request))


@permission_required('edit_stats')
def stats_orgs(request, id):
    st_group = OrgGroup.objects.get(id=int(id))
    return render_to_response('st_grp.html', {'st_group': st_group, },
                              context_instance=RequestContext(request))


@permission_required('edit_stats')
def stats_org(request, id):
    org = Org.objects.get(id=int(id))
    group = org.stat_org.get(orgs=org)
    now = datetime.now().year
    years = {}
    if request.method == 'POST':
        form = NewStatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            year = int(data['year'])
            year = YEAR_CHOICES[year]
            month = data['month']
            calls = data['calls']
            requests = data['requests']
            date = '01 '+month+' '+year
            period = datetime.strptime(date, '%d %m %Y')
            try:
                month_st = org.stat_all.get(period__year=year, period__month=month)
            except Stats.DoesNotExist:
                month_st = None
            if month_st:
                user_created = month_st.user_created
                month_st.delete()
                data = org.stat_all.create(period=period, calls=calls, requests=requests, user_created=user_created, user_changed=request.user)
                data.save()
            else:
                data = org.stat_all.create(period=period, calls=calls, requests=requests, user_created=request.user)
                data.save()
            return HttpResponseRedirect(reverse('stats_org', args=(id,)))
    else:
        form = NewStatForm()
    for key, value in YEAR_CHOICES.items():
        years[key] = int(value)
    context = {'st_org': org, 'year': years, 'current_year': now, 'form': form, 'group': group}
    return render_to_response('st_org.html', context, context_instance=RequestContext(request))


@csrf_exempt
def get_stat(request):
    if request.is_ajax():
        if request.method == 'GET':
            year = int(request.GET.get('year'))
            org_id = int(request.GET.get('org'))
            org = Org.objects.get(id=org_id)
            stats = org.stat_all.filter(period__year=year)
            table_data = json.dumps(
                {
                    "aaData": [{"id": st.period.month,
                                "month": MONTHS[st.period.month].encode('utf-8'),
                                "calls": st.calls,
                                "requests": st.requests,
                               }
                               for st in stats]
                }, ensure_ascii=False)
            return HttpResponse(table_data, 'application/javascript')
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


#------------------- Charts -------------------#
from chartit import DataPool, Chart

from django.utils.dateformat import format


def requests_chart_view(request, id):
    org = Org.objects.get(id=int(id))
    group = org.stat_org.get(orgs=org)
    stats = org.stat_all.all()
    requestsdata = \
        DataPool(
            series=
            [{'options': {
                'source': stats},
              'terms': [
                  ('period', lambda d: format(d, "F")),
                  'requests',
                  'calls']}
            ])
    cht = Chart(
        datasource=requestsdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
          'terms': {
              'period': [
                  'requests',
                  'calls']
          }}],
        chart_options=
        {'title': {
            'text': u'Динамика количества обращений и запросов по месяцам'},
            'xAxis': {'title': {'text': u'Месяц'}},
            'yAxis': {'title': {'text': u'Количество'}}},
        x_sortf_mapf_mts=(lambda *x: (-1*x[0],), None, False))
    return render_to_response('st_chart.html', {'requestchart': cht, 'group': group, 'org': org})
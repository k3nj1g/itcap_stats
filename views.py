# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.dates import MONTHS

import datetime
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
def add_stats(request, id):
    st_org = Org.objects.get(id=int(id))
    return render_to_response('st_org.html', {'st_org': st_org},
                              context_instance=RequestContext(request))


@permission_required('edit_stats')
def stats_org(request, id):
    org = Org.objects.get(id=int(id))
    now = datetime.datetime.now().year
    years = {}
    if request.method == 'POST':
        form = NewStatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            year = int(data['year'])
            year = YEAR_CHOICES[year]
            month = data['month']
            month_st = org.stat_all.filter(period__year=year, period__month=month)
            month_st.delete()
            calls = data['calls']
            requests = data['requests']
            date = '01 '+month+' '+year
            period = datetime.datetime.strptime(date, '%d %m %Y')
            data = org.stat_all.create(period=period, calls=calls, requests=requests, user_created=request.user)
            data.save()
            return HttpResponseRedirect(reverse('stats_org', args=(id,)))
    else:
        form = NewStatForm()
    for key, value in YEAR_CHOICES.items():
        years[key] = int(value)
    return render_to_response('st_org.html', {'st_org': org, 'year': years, 'current_year': now, 'form': form},
                              context_instance=RequestContext(request))


@permission_required('edit_stats')
def add_stats_page(request, id):
    org = Org.objects.get(id=int(id))
    form = NewStatForm()
    return render_to_response('add_st.html', {'org': org, 'form': form},
                              context_instance=RequestContext(request))

@permission_required('edit_stats')
def add_stat(request):
    if request.method == 'POST':
        form = NewStatForm(request.POST)
        id = int(request.POST.get('org'))
        org = Org.objects.get(id=id)
        info = ""
        if form.is_valid():
            data = form.cleaned_data
            year = int(data['year'])
            year = YEAR_CHOICES[year]
            month = data['month']
            month_st = org.stat_all.filter(period__year=year, period__month=month)
            month_st.delete()
            #info = "Статистика за " + str(month) + " месяц перезаписанa"
            #data = Stats.objects.create(year=year, month=month, sum_all=sum_all)
            #data.save()
        return HttpResponseRedirect('ad')


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
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class OrgsAdmin(admin.ModelAdmin):
    filter_horizontal = ('stat_all',)


class OrgGroupAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'orgs']}),
    ]
    list_display = ('name', 'description',)
    filter_horizontal = ('orgs',)


class StatsAdmin(admin.ModelAdmin):
    list_display = ('period', 'calls', 'requests', 'created', 'modified')


admin.site.register(OrgGroup, OrgGroupAdmin)
admin.site.register(Org, OrgsAdmin)
admin.site.register(Stats, StatsAdmin)
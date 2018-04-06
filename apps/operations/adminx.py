# -*- coding: utf-8 -*-

import xadmin
from .models import EquipmentCollection, EquipmentIssue,Demand,SoftwareCollection,SoftwareIssue,TechnologyCollection,TechnologyIssue


class EquipmentCollectionAdmin(object):
    list_display = ['collector',  'product', 'add_time']
    # search_fields = ['collector',  'product', 'add_time']
    list_filter = ['collector',  'product', 'add_time']


class EquipmentIssueAdmin(object):
    list_display = ['issuer',  'product', 'add_time']
    # search_fields = ['issuer',  'product', 'add_time']
    list_filter = ['issuer',  'product', 'add_time']

class DemandAdmin(object):
    list_display = ['demand_id','demander','type', 'title', 'time','money']
    # search_fields = ['demand_id','demander' ,'type', 'title', 'time','money']
    list_filter = ['demand_id', 'type','demander' ,'title', 'time','money']


class SoftwareCollectionAdmin(object):
    list_display = ['collector',  'product', 'add_time']
    # search_fields = ['collector',  'product', 'add_time']
    list_filter = ['collector',  'product', 'add_time']


class SoftwareIssueAdmin(object):
    list_display = ['issuer',  'product', 'add_time']
    # search_fields = ['issuer',  'product', 'add_time']
    list_filter = ['issuer',  'product', 'add_time']


class TechnologyCollectionAdmin(object):
    list_display = ['collector',  'product', 'add_time']
    # search_fields = ['collector',  'product', 'add_time']
    list_filter = ['collector',  'product', 'add_time']


class TechnologyIssueAdmin(object):
    list_display = ['issuer',  'product', 'add_time']
    # search_fields = ['issuer',  'product', 'add_time']
    list_filter = ['issuer',  'product', 'add_time']



xadmin.site.register(EquipmentCollection, EquipmentCollectionAdmin)
xadmin.site.register(EquipmentIssue, EquipmentIssueAdmin)
xadmin.site.register(SoftwareCollection,SoftwareCollectionAdmin)
xadmin.site.register(SoftwareIssue,SoftwareIssueAdmin)
xadmin.site.register(TechnologyCollection,TechnologyCollectionAdmin)
xadmin.site.register(TechnologyIssue,TechnologyIssueAdmin)
xadmin.site.register(Demand,DemandAdmin)

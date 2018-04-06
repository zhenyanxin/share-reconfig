# -*- coding: utf-8 -*-

import xadmin
from .models import EquipmentOrder,SoftwareOrder,TechnologyOrder



class EquipmentOrderAdmin(object):
    list_display = ['order_id', 'product','payer', 'payee','payment_method']
    search_fields = ['order_id', 'product','payer', 'payee','payment_method']
    list_filter = ['order_id', 'product','payer', 'payee','payment_method']



class SoftwareOrderAdmin(object):
    list_display = ['order_id', 'product','payer', 'payee','payment_method']
    # search_fields = ['order_id', 'product','payer', 'payee','payment_method']
    list_filter = ['order_id', 'product','payer', 'payee','payment_method']


class TechnologyOrderAdmin(object):
    list_display = ['order_id', 'product','payer', 'payee','payment_method']
    # search_fields = ['order_id', 'product','payer', 'payee','payment_method']
    list_filter = ['order_id', 'product','payer', 'payee','payment_method']


xadmin.site.register(EquipmentOrder, EquipmentOrderAdmin)
xadmin.site.register(SoftwareOrder, SoftwareOrderAdmin)
xadmin.site.register(TechnologyOrder,TechnologyOrderAdmin)

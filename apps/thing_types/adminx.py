# _*_ coding:utf-8 _*_
from .models import EquipmentType, SoftwareType, TechnologyType
import xadmin


class EquipmentTypeAdmin(object):
    list_display = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    # search_fields = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    list_filter = ['type_name', 'type_grade','parent_grade','is_tab','add_time']


class SoftwareTypeAdmin(object):
    list_display = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    # search_fields = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    list_filter = ['type_name', 'type_grade','parent_grade','is_tab','add_time']


class TechnologyTypeAdmin(object):
    list_display = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    # search_fields = ['type_name', 'type_grade','parent_grade','is_tab','add_time']
    list_filter = ['type_name', 'type_grade','parent_grade','is_tab','add_time']


xadmin.site.register(EquipmentType, EquipmentTypeAdmin)
xadmin.site.register(SoftwareType, SoftwareTypeAdmin)
xadmin.site.register(TechnologyType, TechnologyTypeAdmin)

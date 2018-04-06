#-*-coding:utf-8-*-

import django_filters
from .models import Equipment, EquipmentOrder


class EquipmentOrderFilter(django_filters.rest_framework.FilterSet):
    """

    """
    order_id = django_filters.NumberFilter(name="order_id")
    payer = django_filters.CharFilter(name="payer__user_name")
    class Meta:
        model = EquipmentOrder
        fields = ["order_id","payer"]

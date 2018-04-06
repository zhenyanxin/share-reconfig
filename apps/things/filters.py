#-*-coding:utf-8-*-

import django_filters
from .models import Equipment, Software, Technology


class EquipmentFilter(django_filters.rest_framework.FilterSet):
    """

    """
    price_min = django_filters.NumberFilter(name="equip_price",lookup_expr="gte")
    price_max = django_filters.NumberFilter(name="equip_price", lookup_expr="lte")
    time_start_greater = django_filters.DateTimeFilter(name="equip_start",lookup_expr="gte")
    time_start_less = django_filters.DateTimeFilter(name="equip_start",lookup_expr="lte")
    time_end_greater = django_filters.DateTimeFilter(name="equip_end", lookup_expr="gte")
    time_end_less = django_filters.DateTimeFilter(name="equip_end", lookup_expr="lte")
    equip_owner_name=django_filters.CharFilter(name="equip_owner_ _user_name")
    equip_owner_phone=django_filters.CharFilter(name="equip_owner__phone")

    class Meta:
        model = Equipment
        fields = ["price_min", "price_max","time_start_greater","time_start_less","time_end_greater","time_end_less","equip_owner"]


class SoftwareFilter(django_filters.rest_framework.FilterSet):
    """

    """
    price_min = django_filters.NumberFilter(name="software_price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(name="software_price", lookup_expr="lte")
    time_start_greater = django_filters.DateTimeFilter(name="software_start", lookup_expr="gte")
    time_start_less = django_filters.DateTimeFilter(name="software_start", lookup_expr="lte")
    time_end_greater = django_filters.DateTimeFilter(name="software_end", lookup_expr="gte")
    time_end_less = django_filters.DateTimeFilter(name="software_end", lookup_expr="lte")

    class Meta:
        model = Software
        fields = ["price_min", "price_max", "time_start_greater", "time_start_less", "time_end_greater",
                  "time_end_less"]


class TechnologyFilter(django_filters.rest_framework.FilterSet):
    """

    """
    price_min = django_filters.NumberFilter(name="tech_price", lookup_expr="gte")
    price_max = django_filters.NumberFilter(name="tech_price", lookup_expr="lte")
    time_start_greater = django_filters.DateTimeFilter(name="tech_start", lookup_expr="gte")
    time_start_less = django_filters.DateTimeFilter(name="tech_start", lookup_expr="lte")
    time_end_greater = django_filters.DateTimeFilter(name="tech_end", lookup_expr="gte")
    time_end_less = django_filters.DateTimeFilter(name="tech_end", lookup_expr="lte")

    class Meta:
        model = Technology
        fields = ["price_min", "price_max", "time_start_greater", "time_start_less", "time_end_greater",
                  "time_end_less"]
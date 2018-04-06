#-*-coding:utf-8-*-

import django_filters
from .models import EquipmentType, SoftwareType, TechnologyType


class EquipmentTypeFilter(django_filters.rest_framework.FilterSet):
    """

    """
    type_name = django_filters.CharFilter(name="type_name")
    type_grade = django_filters.CharFilter(name="type_grade")

    class Meta:
        model = EquipmentType
        fields = ["type_name", "type_grade"]


class SoftwareTypeFilter(django_filters.rest_framework.FilterSet):
    """

    """
    type_name = django_filters.CharFilter(name="type_name")
    type_grade = django_filters.CharFilter(name="type_grade")

    class Meta:
        model = SoftwareType
        fields = ["type_name", "type_grade"]


class TechnologyTypeFilter(django_filters.rest_framework.FilterSet):
    """

    """
    type_name = django_filters.CharFilter(name="type_name")
    type_grade = django_filters.CharFilter(name="type_grade")
    class Meta:
        model = TechnologyType
        fields = ["type_name", "type_grade"]
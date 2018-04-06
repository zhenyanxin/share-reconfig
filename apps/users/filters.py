#-*-coding:utf-8-*-

import django_filters
from .models import Equipment

class UserFilter(django_filters.rest_framework.FilterSet):
    """

    """
    name=django_filters.CharFilter("name",lookup_expr="icontaint")
    phone=django_filters.CharFilter("phone")

    class Meta:
        model = Equipment
        fields = ["name","phone"]
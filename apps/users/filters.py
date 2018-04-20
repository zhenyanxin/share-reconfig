# -*-coding:utf-8-*-

import django_filters
from .models import User, VerifyCode


class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤器
    """
    phone = django_filters.CharFilter("phone")

    class Meta:
        model = User
        fields = ["phone"]


class VerifyCodeFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤器
    """
    mobile = django_filters.CharFilter("mobile")

    class Meta:
        model = VerifyCode
        fields = ["mobile"]

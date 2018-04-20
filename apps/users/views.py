# _*_coding:utf-8_*_

# Create your views here.

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import UsersSerializer, VerifyCodesSerializer
from .models import User, VerifyCode
from .filters import UserFilter, VerifyCodeFilter
from django_filters.rest_framework import DjangoFilterBackend


class UserPagination(PageNumberPagination):
    """
    用户分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UsersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView,generics.UpdateAPIView):
    """
    用户数据列表
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = UserPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserFilter


class VerifyCodePagination(PageNumberPagination):
    """
    验证码分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class VerifyCodesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView,generics.UpdateAPIView):
    """
    验证码记录列表
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodesSerializer
    pagination_class = VerifyCodePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = VerifyCodeFilter

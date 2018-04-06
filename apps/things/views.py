#-*-coding:utf-8-*-
from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from .serializers import EquipmentsSerializer,SoftwaresSerializer,TechnologiesSerializer
from .models import Equipment,Software,Technology
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EquipmentFilter,SoftwareFilter,TechnologyFilter

class SoftwarePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SoftwaresViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Software.objects.all()
    serializer_class = SoftwaresSerializer
    pagination_class = SoftwarePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = SoftwareFilter

    search_fields = ('software_name', 'software_place', 'software_parameter', 'software_comment')
    ordering_fields=('software_price','software_expense','software_start','software_end')


class TechnologyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class TechnologiesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    技术列表
    """
    queryset = Technology.objects.all()
    serializer_class = TechnologiesSerializer
    pagination_class = TechnologyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = TechnologyFilter

    search_fields = ('tech_name', 'tech_place', 'tech_parameter', 'tech_comment')
    ordering_fields=('tech_price','tech_expense','tech_start','tech_end')


class EquipmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class EquipmentsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView,generics.UpdateAPIView):
    """
    设备列表
    """
    queryset = Equipment.objects.all()
    serializer_class = EquipmentsSerializer

    pagination_class = EquipmentPagination

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = EquipmentFilter

    search_fields=('equip_name','equip_place','equip_parameter','equip_comment')
    ordering_fields=('equip_price','equip_expense','equip_start','equip_end')


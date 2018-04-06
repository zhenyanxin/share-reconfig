from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

from .filters import EquipmentOrderFilter
from .serializers import SoftwareOrdersSerializer,TechnologyOrdersSerializer,EquipmentOrdersSerializer
from .models import EquipmentOrder,TechnologyOrder,SoftwareOrder

class EquipmentOrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class EquipmentOrdersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = EquipmentOrder.objects.all()
    serializer_class = EquipmentOrdersSerializer
    pagination_class = EquipmentOrderPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = EquipmentOrderFilter

    search_fields = ('order_id',)
    ordering_fields=('pay_time',)


class TechnologyOrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class TechnologyOrdersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = TechnologyOrder.objects.all()
    serializer_class = TechnologyOrdersSerializer
    pagination_class = TechnologyOrderPagination


class SoftwareOrderPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SoftwareOrdersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = SoftwareOrder.objects.all()
    serializer_class = SoftwareOrdersSerializer
    pagination_class = SoftwareOrderPagination
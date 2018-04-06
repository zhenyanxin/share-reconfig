# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from thing_types.filters import EquipmentTypeFilter
from .models import SoftwareType,EquipmentType,TechnologyType
from .serializers import TechnologyTypesSerializer,SoftwareTypesSerializer,EquipmentTypesSerializer
from rest_framework import viewsets, mixins
from rest_framework import filters

# Create your views here.


class TechnologyTypesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = TechnologyType.objects.all()
    serializer_class = TechnologyTypesSerializer


class SoftwareTypesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = SoftwareType.objects.all()
    serializer_class = SoftwareTypesSerializer


class EquipmentTypesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypesSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = EquipmentTypeFilter

    search_fields = ('type_name', 'type_grade')
    ordering_fields = ('type_grade',)
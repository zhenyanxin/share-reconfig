from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import EquipmentCollectionsSerializer, EquipmentIssuesSerializer,SoftwareCollectionsSerializer,SoftwareIssuesSerializer,TechnologyCollectionsSerializer,TechnologyIssuesSerializer, DemandsSerializer
from .models import EquipmentIssue,SoftwareIssue,TechnologyIssue,EquipmentCollection,SoftwareCollection,TechnologyCollection,Demand


#Equipment
class EquipmentCollectionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class EquipmentCollectionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = EquipmentCollection.objects.all()
    serializer_class = EquipmentCollectionsSerializer
    pagination_class = EquipmentCollectionPagination


class EquipmentIssuePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class EquipmentIssuesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = EquipmentIssue.objects.all()
    serializer_class = EquipmentIssuesSerializer
    pagination_class = EquipmentIssuePagination


#Software
class SoftwareCollectionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SoftwareCollectionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = SoftwareCollection.objects.all()
    serializer_class = SoftwareCollectionsSerializer
    pagination_class = SoftwareCollectionPagination


class SoftwareIssuePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SoftwareIssuesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = SoftwareIssue.objects.all()
    serializer_class = SoftwareIssuesSerializer
    pagination_class = SoftwareIssuePagination


#Technology
class TechnologyCollectionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class TechnologyCollectionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = TechnologyCollection.objects.all()
    serializer_class = TechnologyCollectionsSerializer
    pagination_class = TechnologyCollectionPagination


class TechnologyIssuePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class TechnologyIssuesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = TechnologyIssue.objects.all()
    serializer_class = TechnologyIssuesSerializer
    pagination_class = TechnologyIssuePagination


#demand
class DemandPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class DemandsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Demand.objects.all()
    serializer_class = DemandsSerializer
    pagination_class = DemandPagination
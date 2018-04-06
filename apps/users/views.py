
from django.shortcuts import render

# Create your views here.

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from .serializers import UsersSerializer,VerifyCodesSerializer
from .models import User,VerifyCode



class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class UsersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    pagination_class = UserPagination



class VerifyCodePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class VerifyCodesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, generics.CreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodesSerializer
    pagination_class = VerifyCodePagination

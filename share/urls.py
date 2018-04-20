# _*_ encoding:utf-8 _*_

"""ss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from share.settings import MEDIA_ROOT
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from things.views import EquipmentsViewSet, SoftwaresViewSet, TechnologiesViewSet
from thing_types.views import TechnologyTypesView, SoftwareTypesView, EquipmentTypesView
from users.views import UsersViewSet, VerifyCodesViewSet
from operations.views import EquipmentIssuesViewSet, EquipmentCollectionsViewSet, SoftwareCollectionsViewSet, \
    SoftwareIssuesViewSet, TechnologyCollectionsViewSet, TechnologyIssuesViewSet, DemandsViewSet
from django.views.static import serve
from orders.views import EquipmentOrdersViewSet, TechnologyOrdersViewSet, SoftwareOrdersViewSet

router = DefaultRouter()

router.register(r'equipments', EquipmentsViewSet)
router.register(r'softwares', SoftwaresViewSet)
router.register(r'technologies', TechnologiesViewSet)
router.register(r'equipment_issue', EquipmentIssuesViewSet)
router.register(r'equipment_collection', EquipmentCollectionsViewSet)
router.register(r'software_issue', SoftwareIssuesViewSet)
router.register(r'software_collection', SoftwareCollectionsViewSet)
router.register(r'technology_issue', TechnologyIssuesViewSet)
router.register(r'technology_collection', TechnologyCollectionsViewSet)
router.register(r'demand', DemandsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'verifyCodes', VerifyCodesViewSet)
router.register(r'equipment_orders', EquipmentOrdersViewSet)
router.register(r'software_orders', SoftwareOrdersViewSet)
router.register(r'technology_orders', TechnologyOrdersViewSet)
router.register(r'technology_types', TechnologyTypesView)
router.register(r'software_types', SoftwareTypesView)
router.register(r'equipment_types', EquipmentTypesView)

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),

    url(r'docs/', include_docs_urls(title='地质设备共享')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

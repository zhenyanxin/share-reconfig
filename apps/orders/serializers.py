#-*-coding:utf-8-*-
from rest_framework import serializers
from orders.models import EquipmentOrder,TechnologyOrder,SoftwareOrder
from users.serializers import UsersSerializer
from things.serializers import EquipmentsSerializer,SoftwaresSerializer,TechnologiesSerializer
from thing_types.serializers import EquipmentTypesSerializer,SoftwareTypesSerializer,TechnologyTypesSerializer

class EquipmentOrdersSerializer(serializers.ModelSerializer):
    payer=UsersSerializer()
    payee=UsersSerializer()
    product=EquipmentsSerializer()
    class Meta:
        model = EquipmentOrder
        fields="__all__"

    def create(self, validated_data):
        return EquipmentOrder.objects.create(**validated_data)


class SoftwareOrdersSerializer(serializers.ModelSerializer):
    payer = UsersSerializer()
    payee = UsersSerializer()
    product = SoftwaresSerializer()
    class Meta:
        model = SoftwareOrder
        fields="__all__"

    def create(self, validated_data):
        return SoftwareOrder.objects.create(**validated_data)


class TechnologyOrdersSerializer(serializers.ModelSerializer):
    payer = UsersSerializer()
    payee = UsersSerializer()
    product = TechnologiesSerializer()
    class Meta:
        model = TechnologyOrder
        fields="__all__"

    def create(self, validated_data):
        return TechnologyOrder.objects.create(**validated_data)
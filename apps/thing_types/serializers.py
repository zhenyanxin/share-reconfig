#-*-coding:utf-8-*-
from rest_framework import serializers
from thing_types.models import TechnologyType,EquipmentType,SoftwareType



class SoftwareTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareType
        fields="__all__"


class TechnologyTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyType
        fields="__all__"


class EquipmentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields="__all__"

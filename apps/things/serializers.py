# -*-coding:utf-8-*-

from rest_framework import serializers
from things.models import Equipment, Software, Technology
from thing_types.serializers import EquipmentTypesSerializer, SoftwareTypesSerializer, TechnologyTypesSerializer
from users.serializers import UsersSerializer


class EquipmentsSerializer(serializers.ModelSerializer):
    equip_type = EquipmentTypesSerializer()
    equip_owner = UsersSerializer()

    class Meta:
        model = Equipment
        fields = "__all__"

    # 2018/3/29
    def create(self, validated_data):
        equip_type = validated_data.pop('equip_type')
        equip_owner = validated_data.pop('equip_owner')
        return Equipment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Equipment.objects.update(**validated_data)


class SoftwaresSerializer(serializers.ModelSerializer):
    software_type = SoftwareTypesSerializer()
    software_owner = UsersSerializer()

    class Meta:
        model = Software
        fields = "__all__"

    def create(self, validated_data):
        return Software.objects.create(**validated_data)


class TechnologiesSerializer(serializers.ModelSerializer):
    tech_type = TechnologyTypesSerializer()
    tech_owner = UsersSerializer()

    class Meta:
        model = Technology
        fields = "__all__"

    def create(self, validated_data):
        return Technology.objects.create(**validated_data)

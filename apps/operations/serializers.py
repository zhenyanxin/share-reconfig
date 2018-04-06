#-*-coding:utf-8-*-
from rest_framework import serializers
from operations.models import EquipmentIssue,SoftwareIssue,TechnologyIssue,EquipmentCollection,SoftwareCollection,TechnologyCollection,Demand
from things.serializers import EquipmentsSerializer,SoftwaresSerializer,TechnologiesSerializer

from users.serializers import UsersSerializer


#equipment
class EquipmentCollectionsSerializer(serializers.ModelSerializer):
    collector=UsersSerializer()
    product=EquipmentsSerializer()
    class Meta:
        model = EquipmentCollection
        fields="__all__"

    def create(self, validated_data):
        return EquipmentCollection.objects.create(**validated_data)


class EquipmentIssuesSerializer(serializers.ModelSerializer):
    issuer=UsersSerializer()
    product=EquipmentsSerializer()
    class Meta:
        model = EquipmentIssue
        fields="__all__"

    def create(self, validated_data):
        return EquipmentIssue.objects.create(**validated_data)

#Software
class SoftwareCollectionsSerializer(serializers.ModelSerializer):
    collector=UsersSerializer()
    product = SoftwaresSerializer()
    class Meta:
        model = SoftwareCollection
        fields="__all__"

    def create(self, validated_data):
        return SoftwareCollection.objects.create(**validated_data)


class SoftwareIssuesSerializer(serializers.ModelSerializer):
    issuer=UsersSerializer()
    product = SoftwaresSerializer()
    class Meta:
        model = SoftwareIssue
        fields="__all__"

    def create(self, validated_data):
        return SoftwareIssue.objects.create(**validated_data)


#TECHNOLOGY
class TechnologyCollectionsSerializer(serializers.ModelSerializer):
    collector = UsersSerializer()
    product = TechnologiesSerializer()
    class Meta:
        model = TechnologyCollection
        fields = "__all__"

    def create(self, validated_data):
        return TechnologyCollection.objects.create(**validated_data)

class TechnologyIssuesSerializer(serializers.ModelSerializer):
    issuer = UsersSerializer()
    product = TechnologiesSerializer()
    class Meta:
        model = TechnologyIssue
        fields = "__all__"

    def create(self, validated_data):
        return TechnologyIssue.objects.create(**validated_data)


class DemandsSerializer(serializers.ModelSerializer):
    demander=UsersSerializer()
    class Meta:
        model = Demand
        fields="__all__"

    def create(self, validated_data):
        return Demand.objects.create(**validated_data)
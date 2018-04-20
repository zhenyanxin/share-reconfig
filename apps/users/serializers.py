# -*-coding:utf-8-*-

from rest_framework import serializers
from .models import User, VerifyCode


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class VerifyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = "__all__"

    def create(self, validated_data):
        return VerifyCode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        修改用户信息
        :param instance:
        :param validated_data:
        :return:
        """
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.code = validated_data.get('code', instance.code)
        instance.add_time = validated_data.get('add_time', instance.add_time)
        instance.save()
        return instance

    def to_representation(self, instance):
        ret = super(VerifyCodesSerializer, self).to_representation(instance);
        ret["mobile"] = instance.mobile
        return ret

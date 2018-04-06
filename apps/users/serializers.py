#-*-coding:utf-8-*-

from rest_framework import serializers
from .models import User,VerifyCode


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields="__all__"

    def create(self, validated_data):
        return User.objects.create(**validated_data)




class VerifyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields="__all__"

    def create(self, validated_data):
        return VerifyCode.objects.create(**validated_data)
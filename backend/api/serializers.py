from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
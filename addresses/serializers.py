from rest_framework import serializers
from .models import Address
from users.serializers import UserSerializer
import ipdb


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)

    def update(self, instance: Address, validated_data: dict) -> Address:

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ['street', 'number', 'city', 'user']

from rest_framework import serializers
from .models import Address
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)

    def update(self, instance: Address, validated_data: dict) -> Address:
        address = get_object_or_404(Address, user=instance)
        for key, value in validated_data.items():
            setattr(address, key, value)

        address.save()
        return address

    user = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ['street', 'number', 'city', 'user']

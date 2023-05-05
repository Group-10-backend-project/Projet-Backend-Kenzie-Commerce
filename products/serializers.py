from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Product:
        user = self.context['request'].user
        validated_data['user'] = user
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'amount',
            'price',
            'user_id',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'user_id': {'read_only': True},
        }

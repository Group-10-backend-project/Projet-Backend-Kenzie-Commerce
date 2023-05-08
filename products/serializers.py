from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
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

    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'amount',
            'price',
            'category',
            'user_id',
            'is_available',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'user_id': {'read_only': True},
        }

    def get_is_available(self, obj):
        return obj.amount > 0

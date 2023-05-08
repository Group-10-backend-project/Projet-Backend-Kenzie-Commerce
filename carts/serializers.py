from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer
import ipdb


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['is_active', "products", "user_id"]

    def create(self, validated_data):
        return Cart.objects.create(**validated_data)

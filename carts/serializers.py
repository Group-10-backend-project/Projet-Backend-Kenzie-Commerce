from rest_framework import serializers
from .models import CartProduct, Cart
from users.models import User
from products.models import Product
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class CartProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.pop('user')
        cart = Cart.objects.filter(user=user, is_active=True)

        if not cart:
            cart = Cart.objects.create(user=user)
        else:
            cart = cart[0]

        validated_data['cart'] = cart

        return CartProduct.objects.create(**validated_data)

    user = UserSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ['amount', 'user', 'products_id']
        extra_kwargs = {
            'products_id': {'source': 'products'}
        }


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = ['is_active', 'user', 'products']
        extra_kwargs = {
            'is_active': {'read_only': True}
        }

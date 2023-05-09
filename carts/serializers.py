from rest_framework import serializers
from .models import CartProduct, Cart
from users.models import User
from products.models import Product
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
import ipdb


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = ['amount', 'products']

    def create(self, validated_data):

        user = validated_data.pop('user')
        cart = Cart.objects.filter(user=user, is_active=True)

        if not cart:
            cart = Cart.objects.create(user=user)
        else:
            cart = cart[0]

        validated_data['cart'] = cart
        cart_product = CartProduct.objects.create(**validated_data)
        serialized_product = ProductSerializer(validated_data['products']).data
        serialized_product['amount'] = cart_product.amount
        return {**validated_data, 'products_id': serialized_product}


class CartSerializer(serializers.ModelSerializer):
    cart_products = CartProductSerializer(many=True, read_only=True)
    user = UserSerializer()

    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['is_active', 'user', 'products', 'cart_products']
        extra_kwargs = {
            'is_active': {'read_only': True}
        }

    def validate(self, data):
        if not Product.objects.filter(id=data['products'].id).exists():
            raise serializers.ValidationError('Invalid product ID')
        return data

    def get_products(self, obj):
        cart_products = obj.cartproduct_set.all()
        return [self.get_product_data(product) for product in cart_products]

    def get_product_data(self, cart_product):
        product = cart_product.products
        serialized_product = ProductSerializer(product).data
        serialized_product['amount'] = cart_product.amount
        return serialized_product

    def create(self, validated_data):
        user = self.context['request'].user
        return Cart.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

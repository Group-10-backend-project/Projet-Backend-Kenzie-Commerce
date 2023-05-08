from rest_framework import serializers
from .models import CartProduct, Cart
from users.models import User
from products.models import Product
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
import ipdb


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Cart
        fields = ['is_active', 'user', 'products']
        extra_kwargs = {
            'is_active': {'read_only': True}
        }


class CartProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)

        cart = Cart.objects.filter(user=user, is_active=True)[0]

        if not cart:
            cart = Cart.objects.create(user=user)

        validated_data['cart'] = cart

        return CartProduct.objects.create(**validated_data)

    user = UserSerializer(read_only=True)

    class Meta:
        model = CartProduct
        fields = ['amount', 'user', 'products_id']
        extra_kwargs = {
            'products_id': {'source': 'products'}
        }

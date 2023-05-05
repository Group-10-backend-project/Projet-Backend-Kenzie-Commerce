from rest_framework import serializers
from .models import Order, OrderOptions


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    model = Order
    fields = ["created_at"]

    extra_kwargs = {
        "status": {
            serializers.ChoiceField(choices=OrderOptions, default=OrderOptions.DEFAULT)
        }
    }

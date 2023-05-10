from rest_framework import serializers
from .models import Order, OrderOptions
from django.core.mail import send_mail
from django.conf import settings
import ipdb


class OrderSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        ipdb.set_trace()
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        email = instance
        for key, value in validated_data.items():
            if True:
                send_mail(
                    subject="Subject here",
                    message=" PEDIDO REALIZADO ",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[
                        "fernandorazer.16@gmail.com",
                        "renan.giaretta@hotmail.com",
                        "jonatasilveira04@gmail.com",
                    ],
                    fail_silently=False,
                )

            setattr(instance, key, value)
            instance.save()

        return instance

    model = Order
    fields = ["created_at", "user_id", "cart_id", "saller_id"]

    extra_kwargs = {
        "status": {
            serializers.ChoiceField(choices=OrderOptions, default=OrderOptions.DEFAULT)
        }
    }

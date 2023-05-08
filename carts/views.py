from django.shortcuts import render
from rest_framework import generics
from .models import Cart, CartProduct
from utils.mixins import SerializerByMethodMixin
from .serializers import CartSerializer, CartProductSerializer
import ipdb

# Create your views here.


class CartView(SerializerByMethodMixin, generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_map = {
        'GET': CartSerializer,
        'POST': CartProductSerializer
    }

    def perform_create(self, serializer):
        return serializer.save(
            user_id=self.kwargs.get("user_id")
        )

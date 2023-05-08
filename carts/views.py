from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer
import ipdb

# Create your views here.


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs.get("user_id"))

from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer

# Create your views here.


class CartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
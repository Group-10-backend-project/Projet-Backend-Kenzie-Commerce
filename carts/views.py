from django.shortcuts import render
from rest_framework import generics
from .models import Cart, CartProduct
from utils.mixins import SerializerByMethodMixin
from .serializers import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb

# Create your views here.


class CartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    lookup_field = 'user_id'

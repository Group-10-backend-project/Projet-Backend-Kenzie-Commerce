from django.shortcuts import render
from rest_framework import generics
from .models import Cart, CartProduct
from .serializers import CartSerializer, CartProductSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsCartOwner, IsSellerOrAdmin


class CartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwner]

    queryset = Cart.objects.all()
    serializer_class = CartProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCartOwner | IsSellerOrAdmin]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    lookup_field = 'user_id'

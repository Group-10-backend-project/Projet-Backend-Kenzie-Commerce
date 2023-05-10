from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from carts.models import Cart

from users.models import User
from .serializers import OrderSerializer
from .models import Order
import ipdb


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        saller = get_object_or_404(User, id=self.request.data["user_id"])
        cart = get_object_or_404(Cart, id=self.request.data["cart_id"])
        serializer.save(user=self.request.user, cart=cart, saller=saller)
        return super().perform_create(serializer)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from users.models import User
from .serializers import OrderSerializer
from .models import Order
import ipdb


class OrderView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        ipdb.set_trace()
        logged_user = get_object_or_404(User, id=self.request.user.id)
        serializer.save(user=logged_user)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

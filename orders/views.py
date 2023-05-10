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
        user = self.context["request"].user
        body = self.context["request"].body
        print(user)
        ipdb.set_trace()
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

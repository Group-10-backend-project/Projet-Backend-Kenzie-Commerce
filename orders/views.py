from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import OrderSerializer


class OrderView(ListCreateAPIView):
    serializer_class = OrderSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #     return super().perform_create(serializer)

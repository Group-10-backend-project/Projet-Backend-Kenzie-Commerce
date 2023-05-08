from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
import ipdb


class AddressView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user_id=self.kwargs.get("user_id"))


class AddressDetailView(generics.RetrieveUpdateAPIView):
    ...

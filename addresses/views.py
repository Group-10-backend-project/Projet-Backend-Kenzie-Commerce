from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
import ipdb


class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        ipdb.set_trace()
        return serializer.save(user_id=self.kwargs.get("user_id"))


class AddressDetailView(generics.RetrieveUpdateAPIView):
    ...

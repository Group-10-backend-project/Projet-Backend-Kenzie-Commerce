from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import ipdb


class AddressView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateAPIView):
    ...

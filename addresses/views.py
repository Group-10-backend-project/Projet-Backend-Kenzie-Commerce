from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.models import User


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = User.objects.all()
    serializer_class = AddressSerializer

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)

    lookup_url_kwarg = 'user_id'

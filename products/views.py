from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from rest_framework.filters import SearchFilter
from users.permissions import IsSellerOrAdmin, IsProductOwnerOrAdmin
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ProductClientView(generics.ListAPIView):
    serializer_class = ProductSerializer
    search_fields = ['id', 'name', 'category']
    filter_backends = [SearchFilter]
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category__icontains=category)
        prod_id = self.request.query_params.get('id', None)
        if prod_id is not None:
            queryset = queryset.filter(id__icontains=prod_id)
        return queryset


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsSellerOrAdmin,
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        IsAuthenticated,
        IsProductOwnerOrAdmin
    ]

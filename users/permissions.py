from rest_framework import permissions
from .models import User
from rest_framework.views import View
from products.models import Product


class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (request.user.is_authenticated and
                (request.user.is_seller or request.user.is_superuser))


class IsProductOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product) -> bool:
        return obj.user == request.user or request.user.is_superuser

from rest_framework import permissions
from users.models import User
from rest_framework.views import View
from carts.models import Cart


class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Cart):
        return obj.user == request.user


class IsSellerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (request.user.is_authenticated and
                (request.user.is_seller or request.user.is_superuser))

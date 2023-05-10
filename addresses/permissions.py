from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsUserOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User):
        return obj == request.user or request.user.is_superuser

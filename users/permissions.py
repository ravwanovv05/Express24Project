from rest_framework.permissions import BasePermission
from users.roles import UserRole


class IsAdminPermission(BasePermission):

    def has_permission(self, request, view):
        try:
            admin_role = UserRole.objects.get(user=request.user).role.title
        except UserRole.DoesNotExist:
            return False
        return admin_role.lower() == 'admin'


class IsCourierPermissions(BasePermission):

    def has_permission(self, request, view):
        try:
            courier_role = UserRole.objects.get(user=request.user).role.title
        except UserRole.DoesNotExist:
            return False
        return courier_role.lower() == 'courier'

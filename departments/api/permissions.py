from rest_framework.permissions import BasePermission
from accounts.permissions import IsAdminOrManager


class DepartmentManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in ["GET", "HEAD", "OPTION"]:
            return True

        return IsAdminOrManager().has_permission(request, view)


    def has_object_permission(self, request, view, obj):
        if request.user.role == "ADMIN":
            return True

        if request.user.role == "MANAGER":
            return obj.manager.user == request.user

        return False

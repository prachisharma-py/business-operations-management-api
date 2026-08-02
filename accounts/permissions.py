from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to Admin users.
    """

    def has_permission(self, request, view):
        return request.user.role == "ADMIN"


class IsAdminOrManager(BasePermission):
    """
    Allows access only to Admins and Managers.
    """

    def has_permission(self, request, view):
        return request.user.role in ["ADMIN", "MANAGER"]


class EmployeeOwner(BasePermission):
    """
    Employees can access only their own employee profile.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


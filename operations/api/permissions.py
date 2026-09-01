from rest_framework.permissions import BasePermission
from accounts.permissions import IsAdminOrManager


class OperationPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in ["GET", "HEAD", "OPTION"]:
            return True

        if request.method in ["POST", "PUT", "PATCH"]:
            return IsAdminOrManager().has_permission(request, view)

        if request.method == "DELETE":
            return request.user.role == "ADMIN"

        return False


    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "HEAD", "OPTION"]:
            return True

        if request.user.role == "ADMIN":
            return True

        if request.user.role == "MANAGER":
            employee = getattr(request.user, "employee_profile", None)

            if employee is None:
                return False
            
            return obj.department_id == employee.department_id

        return False

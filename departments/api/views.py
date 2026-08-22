from rest_framework import viewsets

from departments.models import Department
from departments.api.serializers import DepartmentReadSerializer, DepartmentWriteSerializer

from departments.api.permissions import DepartmentManagerPermission

# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [DepartmentManagerPermission]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return DepartmentReadSerializer

        return DepartmentWriteSerializer

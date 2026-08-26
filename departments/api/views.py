from django.db.models.deletion import ProtectedError

from rest_framework import viewsets, status
from rest_framework.response import Response

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


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            self.perform_destroy(instance)
        except ProtectedError:
            return Response(
                {
                    "detail": (
                        "Cannot delete department because employees are assigned to it."
                    )
                },
                status=status.HTTP_409_CONFLICT,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)

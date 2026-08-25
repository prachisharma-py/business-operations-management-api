from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from employees.models import Employee
from accounts.permissions import IsAdmin, IsAdminOrManager, EmployeeOwner
from .serializers import EmployeeReadSerializer, EmployeeWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import EmployeeFilter
from common.pagination import StandardResultSetPagination
from common.responses import success_response

from drf_spectacular.utils import extend_schema

import logging


logger = logging.getLogger(__name__)



@extend_schema(
    summary="List and create employees",
    description=(
        "Retrive a paginated list of employees or create a new employee."
        "Only administrators are allowed to create employees."
    ),
    tags=["Employees"],
)

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related("user").all()
    pagination_class = StandardResultSetPagination
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = EmployeeFilter

    search_fields = (
        "employee_id",
        "department__name",
        "designation",
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )

    ordering_fields = (
        "employee_id",
        "joining_date",
        "created_at",
        "department__name",
        "designation",
    )

    ordering = ("-created_at",)

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsAdminOrManager()]
        
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeReadSerializer
        
        return EmployeeWriteSerializer
    
    def list(self, request, *args, **kwargs):
        logger.info("Employee list requested")
        return super().list(request, *args, **kwargs)
    


@extend_schema(
    summary="Retrive, update or delete an employee",
    description=(
        "Retrive employee details, update employee information, or delete an employee. Access is controlled by object-level permissions."
    ),
    tags=["Employees"],
)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related("user").all()
    lookup_field = "pk"

    def get_permissions(self):
        if self.request.method == "DELETE":
            return [IsAuthenticated(), IsAdmin()]
        
        if self.request.method in ["PUT", "PATCH"]:
            return [IsAuthenticated(), IsAdminOrManager()]
        
        if (
            self.request.user.is_authenticated
            and self.request.user.role == "EMPLOYEE"
        ):
            return [IsAuthenticated(), EmployeeOwner()]
        
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return EmployeeReadSerializer
        
        return EmployeeWriteSerializer
    
    def get_object(self):
        obj = super().get_object()

        if (
            self.request.user.is_authenticated
            and self.request.user.role == "EMPLOYEE"
        ):
            self.check_object_permissions(self.request, obj)

        return obj


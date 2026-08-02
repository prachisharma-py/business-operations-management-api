from django_filters import rest_framework as filters
from employees.models import Employee


class EmployeeFilter(filters.FilterSet):

    class Meta:
        model = Employee
        fields = (
            "department",
            "employee_status",
        )


from django_filters import rest_framework as filters
from employees.models import Employee


class EmployeeFilter(filters.FilterSet):

    department = filters.CharFilter(
        field_name="department__name",
        lookup_expr="iexact",
    )

    class Meta:
        model = Employee
        fields = (
            "department",
            "employee_status",
        )


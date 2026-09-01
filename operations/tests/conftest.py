import pytest

from operations.models import Operation


@pytest.fixture
def operation(engineering_department, employee):
    employee.department = engineering_department
    employee.save()

    return Operation.objects.create(
        title="Server Maintenance",
        description="Perform scheduled server maintenance.",
        department=engineering_department,
        assigned_to=employee,
        status=Operation.PENDING,
    )


@pytest.fixture
def finance_operation(finance_department, second_manager_employee):
    return Operation.objects.create(
        title="Finance Report",
        description="Prepare monthly finance report.",
        department=finance_department,
        assigned_to=second_manager_employee,
        status=Operation.PENDING,
    )

import pytest

from operations.models import Operation


@pytest.fixture
def operation(engineering_department, employee):
    return Operation.objects.create(
        title="Server Maintenance",
        description="Perform scheduled server maintenance.",
        department=engineering_department,
        assigned_to=employee,
        status=Operation.PENDING,
    )

@pytest.mark.django_db
def test_operation_creation(operation):
    assert operation.title == "Server Maintenance"
    assert operation.status == Operation.PENDING
    assert operation.department.name == "Engineering"
    assert operation.assigned_to.employee_id == "EMP001"


@pytest.mark.django_db
def test_operation_default_status(engineering_department, employee):
    operation = Operation.objects.create(
        title="Database Backup",
        description="Perform database backup.",
        department=engineering_department,
        assigned_to=employee,
    )

    assert operation.status == Operation.PENDING


@pytest.mark.django_db
def test_operation_can_be_unassigned(engineering_department):
    operation = Operation.objects.create(
        title="Unassigned Task",
        description="Task waiting for assignement",
        department=engineering_department,
        assigned_to=None,
    )

    assert operation.assigned_to is None


@pytest.mark.django_db
def test_operation_str(operation):
    assert str(operation) == "Server Maintenance"

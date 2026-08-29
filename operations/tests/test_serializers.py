import pytest

from operations.api.serializers import OperationWriteSerializer
from operations.models import Operation


@pytest.mark.django_db
def test_operation_serializer_valid(engineering_department, employee):

    data = {
        "title": "Server Maintenance",
        "description": "Perform scheduled maintenance",
        "department": engineering_department.id,
        "assigend_to": employee.id,
        "status": Operation.PENDING,
    }

    serializer = OperationWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_serializer_create_operation(engineering_department, employee):

    data = {
        "title": "Database Backup",
        "description": "Perform database backup.",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.IN_PROGRESS,
    }

    serializer = OperationWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    operation = serializer.save()

    assert operation.title == "Database Backup"
    assert operation.department == engineering_department
    assert operation.assigned_to == employee
    assert operation.status == Operation.IN_PROGRESS


@pytest.mark.django_db
def test_operation_can_be_unassigned(engineering_department):

    data = {
        "title": "Inassigned Task",
        "description": "Task waiting for assignment.",
        "department": engineering_department.id,
        "assigned_to": None,
        "status": Operation.PENDING,
    }

    serializer = OperationWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    operation = serializer.save()

    assert operation.assigned_to is None


@pytest.mark.django_db
def test_employee_from_another_department_cannot_be_assigned(engineering_department, finance_department, employee):
    employee.department = finance_department
    employee.save()

    data = {
        "title": "Engineering Task",
        "description": "Engineering operation",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.PENDING,
    }

    serializer = OperationWriteSerializer(data=data)

    assert not serializer.is_valid()
    assert "assigned_to" in serializer.errors


@pytest.mark.django_db
def test_employee_from_same_department_can_be_assigned(engineering_department, employee):
    employee.department = engineering_department
    employee.save()

    data = {
        "title": "Engineerring Task",
        "description": "Engineering operation",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.PENDING,
    }

    serializer = OperationWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

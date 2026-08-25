import pytest

from employees.api.serializers import EmployeeWriteSerializer
from departments.models import Department


@pytest.fixture
def department():
    return Department.objects.get(name="Engineering")


@pytest.mark.django_db
def test_employee_serializer_valid(user, department):
    data={
        "user": user.id,
        "employee_id": "EMP002",
        "department": department.id,
        "designation": "Backend Developer",
        "joining_date": "2024-4-1",
        "employee_status": "ACTIVE",
    }

    serializer = EmployeeWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_department_required(user):
    data = {
        "user": user.id,
        "employee_id": "EMP002",
    }

    serializer = EmployeeWriteSerializer(data=data)

    assert not serializer.is_valid()
    assert "department" in serializer.errors


@pytest.mark.django_db
def test_serializer_creates_employee(user, department):
    data = {
        "user": user.id,
        "employee_id": "EMP002",
        "department": department.id,
        "designation": "Backend Developer",
        "joining_date": "2024-4-1",
        "employee_status": "ACTIVE",
    }

    serializer = EmployeeWriteSerializer(data=data)

    assert serializer.is_valid(), serializer.errors

    employee = serializer.save()

    assert employee.employee_id == "EMP002"
    assert employee.department == department

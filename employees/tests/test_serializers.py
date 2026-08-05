import pytest

from employees.api.serializers import EmployeeWriteSerializer


@pytest.mark.django_db
def test_employee_serializer_valid(user):
    data={
        "user": user.id,
        "employee_id": "EMP002",
        "department": "Engineering",
        "designation": "Backend Developer",
        "joining_date": "2024-4-1",
        "employee_status": "ACTIVE",
    }

    serializer = EmployeeWriteSerializer(data=data)

    assert serializer.is_valid()


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
def test_serializer_creates_employee(user):
    data = {
        "user": user.id,
        "employee_id": "EMP002",
        "department": "Engineering",
        "designation": "Backend Developer",
        "joining_date": "2024-4-1",
        "employee_status": "ACTIVE",
    }

    serializer = EmployeeWriteSerializer(data=data)

    assert serializer.is_valid()

    employee = serializer.save()

    assert employee.employee_id == "EMP002"
    assert employee.department == "Engineering"

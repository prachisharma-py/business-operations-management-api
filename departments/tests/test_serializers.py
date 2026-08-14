import pytest

from departments.api.serializers import DepartmentWriteSerializer
from employees.models import Employee


@pytest.mark.django_db
def test_active_employee_can_be_deparment_manager(employee):
    data = {
        "name": "Engineereing",
        "description": "Engineering Department",
        "manager": employee.id,
    }

    serializer = DepartmentWriteSerializer(data=data)

    assert serializer.is_valid()
    assert serializer.validated_data["manager"] == employee


@pytest.mark.django_db
def test_inactive_employee_cannot_be_department_manager(employee):
    employee.employee_status = Employee.INACTIVE
    employee.save()

    data = {
        "name": "Engineering",
        "description": "Engineering Department",
        "manager": employee.id,
    }

    serializer = DepartmentWriteSerializer(data=data)

    assert not serializer.is_valid()
    assert "manager" in serializer.errors
    

@pytest.mark.django_db
def test_resigned_employee_cannot_be_department_manager(employee):
    employee.employee_status = Employee.RESIGNED
    employee.save()

    data = {
        "name": "Engineereing",
        "description": "Engineering Department",
        "manager": employee.id,
    }
            
    serializer = DepartmentWriteSerializer(data=data)
    
    assert not serializer.is_valid()
    assert "manager" in serializer.errors


@pytest.mark.django_db
def test_department_can_be_created_without_manager():
    data = {
        "name": "Finanace",
        "description": "Finanace Department",
        "manager": None,       
    }

    serializer = DepartmentWriteSerializer(data=data)

    assert serializer.is_valid()
    assert serializer.validated_data["manager"] is None

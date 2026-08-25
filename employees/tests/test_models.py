import pytest
from django.contrib.auth import get_user_model

from employees.models import Employee

User = get_user_model()


@pytest.mark.django_db
def test_create_employee(employee):
    assert employee.employee_id == "EMP001"
    assert employee.department.name == "Engineering"
    assert employee.designation == "Backend Developer"
    assert employee.employee_status == Employee.ACTIVE


@pytest.mark.django_db
def test_employee_str(employee):
    assert str(employee) == "EMP001 - Alex Johnson"


@pytest.mark.django_db
def test_employee_user_relationship(employee, user):
    assert employee.user == user

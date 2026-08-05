import datetime

import pytest

from django.contrib.auth import get_user_model
from employees.models import Employee

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="alex",
        email="alex@example.com",
        password="password123",
        first_name="Alex",
        last_name="Johnson"
    )


@pytest.fixture
def employee(user):
    return Employee.objects.create(
        user=user,
        employee_id="EMP001",
        department="Engineering",
        designation="Backend Developer",
        joining_date=datetime.date(2024, 4, 1),
    )

import datetime

import pytest

from django.contrib.auth import get_user_model
from employees.models import Employee
from rest_framework.test import APIClient

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
def admin_user():
    return User.objects.create_user(
        username="admin",
        email="admin@example.com",
        password="password123",
        first_name="Admin",
        last_name="User",
        role="ADMIN",
    )


@pytest.fixture
def manager_user():
    return User.objects.create_user(
        username="manager",
        email="manager@example.com",
        password="password123",
        first_name="Manager",
        last_name="User",
        role="MANAGER",
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


@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def admin_client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client


@pytest.fixture
def manager_client(manager_user):
    client = APIClient()
    client.force_authenticate(user=manager_user)
    return client

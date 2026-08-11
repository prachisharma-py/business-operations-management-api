import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

from employees.models import Employee


User = get_user_model()


@pytest.fixture
def employees(user):
    employee1 = Employee.objects.create(
        user=user,
        employee_id="EMP001",
        department="Engineering",
        designation="Backend Developer",
        joining_date="2023-07-25",
    )

    user2 = User.objects.create_user(
        username="alice",
        email="alice@example.com",
        password="password123",
    )

    employee2 = Employee.objects.create(
        user=user2,
        employee_id="EMP002",
        department="HR",
        designation="HR Manager",
        joining_date="2024-12-02"
    )

    user3 = User.objects.create_user(
        username="bob",
        email="bob@example.com",
        password="password123",
    )

    employee3 = Employee.objects.create(
        user=user3,
        employee_id="EMP003",
        department="Engineering",
        designation="Frontend Developer",
        joining_date="2025-05-15",
    )

    return employee1, employee2, employee3


@pytest.mark.django_db
def test_filter_by_department(authenticated_client, employees):
    url = reverse("employee-list-create")
    response = authenticated_client.get(url, {"department": "Engineering"})

    assert response.status_code == 200

    results = response.data["results"]

    assert len(results) == 2
    assert all(employee["department"] == "Engineering" for employee in results)


@pytest.mark.django_db
def test_search_employee(authenticated_client, employees):
    url = reverse("employee-list-create")
    response = authenticated_client.get(url, {"search": "Backend"})

    assert response.status_code == 200

    results = response.data["results"]

    assert len(results) == 1
    assert results[0]["employee_id"] == "EMP001"


@pytest.mark.django_db
def test_employee_ordering(authenticated_client, employees):
    url = reverse("employee-list-create")
    response = authenticated_client.get(url, {"ordering": "employee_id"})

    assert response.status_code == 200

    results = response.data["results"]

    employee_ids = [employee["employee_id"] for employee in results]

    assert employee_ids == sorted(employee_ids)


@pytest.fixture
def many_employees(user):
    employees = []
    for number in range(1, 13):
        if number == 1:
            current_user = user
        else:
            current_user = User.objects.create_user(
                username=f"user{number}",
                email=f"user{number}@example.com",
                password="password123",
            )

        employee = Employee.objects.create(
            user=current_user,
            employee_id=f"EMP{number:03d}",
            department="Engineering",
            designation="Developer",
            joining_date="2026-04-08",
        )

        employees.append(employee)

    return employees


@pytest.mark.django_db
def test_employee_paginantion(authenticated_client, many_employees):
    url = reverse("employee-list-create")
    response = authenticated_client.get(url, {"page": 1})

    assert response.status_code == 200

    assert "results" in response.data
    assert "count" in response.data
    assert "next" in response.data
    assert "previous" in response.data

    assert response.data["count"] == 12
    assert len(response.data["results"]) == 10
    assert response.data["previous"] is None
    assert response.data["next"] is not None

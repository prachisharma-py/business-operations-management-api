import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from employees.models import Employee
from departments.models import Department


User = get_user_model()


@pytest.mark.django_db
def test_list_employee(authenticated_client, employee):
    url = reverse("employee-list-create")

    response = authenticated_client.get(url)

    assert response.status_code == 200

    assert response.data["count"] == 1
    results = response.data["results"]
    assert len(results) == 1
    assert results[0]["employee_id"] == employee.employee_id


@pytest.mark.django_db
def test_retrieve_employee(authenticated_client, employee):
    url = reverse(
        "employee-detail", 
        kwargs={"pk": employee.pk},
    )

    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert response.data["employee_id"] == employee.employee_id


@pytest.mark.django_db
def test_create_employee(admin_client, finance_department):
    new_user = User.objects.create_user(
        username="Jane",
        email="jane@example.com",
        password="password123",
        first_name="Jane",
        last_name="Smith",
        role="EMPLOYEE",
    )

    data = {
        "user": new_user.id,
        "employee_id": "EMP002",
        "department": finance_department.id,
        "designation": "Accountant",
        "joining_date": "2025-01-11",
        "employee_status": "ACTIVE",
    }

    url = reverse("employee-list-create")

    response = admin_client.post(url, data, format="json")

    assert response.status_code == 201
    assert Employee.objects.filter(employee_id="EMP002").exists()


@pytest.mark.django_db
def test_update_employee(manager_client, employee, hr_department):
    response = manager_client.patch(
        reverse(
            "employee-detail",
            kwargs={"pk": employee.id},
        ),
        {
            "department": hr_department.id,
        },
        format="json",
    )

    assert response.status_code == 200
    employee.refresh_from_db()
    assert employee.department == hr_department


@pytest.mark.django_db
def test_delete_employee(admin_client, employee):
    response = admin_client.delete(
        reverse(
            "employee-detail",
            kwargs={"pk": employee.pk},
        )
    )

    assert response.status_code == 204
    assert not Employee.objects.filter(pk=employee.pk).exists()

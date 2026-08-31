import pytest

from django.urls import reverse
from operations.models import Operation


@pytest.fixture
def operation(engineering_department, employee):
    employee.department = engineering_department
    employee.save()

    return Operation.objects.create(
        title="Server Maintenance",
        description="Perform scheduled server maintenance.",
        department=engineering_department,
        assigned_to=employee,
        status=Operation.PENDING,
    )


@pytest.mark.django_db
def test_list_operations(authenticated_client, operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert response.data[0]["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_retrieve_operation(authenticated_client, operation):
    url = reverse("operation-detail", kwargs={"pk": operation.pk})

    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == operation.id
    assert response.data["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_create_operation(admin_client, engineering_department, employee):
    employee.department = engineering_department
    employee.save()

    data = {
        "title": "Database Backup",
        "description": "Perform database backup.",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.PENDING,
    }

    url = reverse("operation-list")

    response = admin_client.post(url, data, format="json")

    assert response.status_code == 201
    assert response.data["title"] == "Database Backup"
    assert Operation.objects.filter(
        title="Database Backup"
    ).exists()


@pytest.mark.django_db
def test_update_operation(admin_client, operation):
    url = reverse("operation-detail", kwargs={"pk": operation.pk})

    data = {
        "title": "Updated Server Maintenance",
        "description": "Updated maintenance task.",
        "department": operation.department.id,
        "assigned_to": operation.assigned_to.id,
        "status": Operation.IN_PROGRESS,
    }

    response = admin_client.put(url, data, format="json")

    assert response.status_code == 200
    assert response.data["title"] == "Updated Server Maintenance"

    operation.refresh_from_db()

    assert operation.title == "Updated Server Maintenance"
    assert operation.status == Operation.IN_PROGRESS



@pytest.mark.django_db
def test_delete_operation(admin_client, operation):
    url = reverse("operation-detail", kwargs={"pk": operation.pk})

    response = admin_client.delete(url)

    assert response.status_code == 204
    assert not Operation.objects.filter(
        pk=operation.pk
    ).exists()

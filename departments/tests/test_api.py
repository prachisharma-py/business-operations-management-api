import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from departments.models import Department


@pytest.fixture
def department(employee):
    return Department.objects.create(
        name="Engineering",
        description="Engineering Department",
        manager=employee,
    )


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_list_department(api_client, department):
    url = reverse("department-list")

    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Engineering"


@pytest.mark.django_db
def test_retrieve_department(api_client, department):
    url = reverse("department-detail", kwargs={"pk": department.id})

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == department.id
    assert response.data["name"] == "Engineering"
    assert response.data["manager"]["id"] == department.manager.id


@pytest.mark.django_db
def test_create_department(api_client, employee):
    data = {
        "name": "Finance",
        "description": "Finance Department",
        "manager": employee.id,
    }

    url = reverse("department-list")

    response = api_client.post(url, data, format="json")

    assert response.status_code == 201
    assert response.data["name"] == "Finance"
    assert response.data["description"] == "Finance Department"

    assert Department.objects.filter(name="Finance").exists()


@pytest.mark.django_db
def test_update_department(api_client, department,employee):
    url = reverse("department-detail", kwargs={"pk": department.id})

    data = {
        "name": "Updated Engineering",
        "description": "Updated Engineering Department",
        "manager": employee.id,
    }

    response = api_client.put(url, data, format="json")

    assert response.status_code == 200
    assert response.data["name"] == "Updated Engineering"

    department.refresh_from_db()

    assert department.name == "Updated Engineering"
    assert department.description == "Updated Engineering Department"


@pytest.mark.django_db
def test_delete_department(api_client, department):
    url = reverse("department-detail", kwargs={"pk": department.id})

    response = api_client.delete(url)

    assert response.status_code == 204
    assert not Department.objects.filter(pk=department.pk).exists()

import pytest
from django.urls import reverse

from departments.models import Department


@pytest.fixture
def department(engineering_department, employee):
    engineering_department.manager = employee
    engineering_department.save()
    return engineering_department


@pytest.mark.django_db
def test_list_department(api_client, department, employee):
    api_client.force_authenticate(user=employee.user)

    url = reverse("department-list")

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["count"] == 4

    names = {department["name"] for department in response.data["results"]}
    assert names == {"Finance", "Sales", "HR", "Engineering"}


@pytest.mark.django_db
def test_retrieve_department(api_client, department ,employee):
    api_client.force_authenticate(user=employee.user)

    url = reverse("department-detail", kwargs={"pk": department.id})

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == department.id
    assert response.data["name"] == "Engineering"
    assert response.data["manager"]["id"] == department.manager.id


@pytest.mark.django_db
def test_create_department(api_client, employee, manager_user):
    api_client.force_authenticate(user=manager_user)

    data = {
        "name": "Operations",
        "description": "Operations Department",
        "manager": employee.id,
    }

    url = reverse("department-list")

    response = api_client.post(url, data, format="json")

    assert response.status_code == 201
    assert response.data["name"] == "Operations"
    assert response.data["description"] == "Operations Department"

    assert Department.objects.filter(name="Operations").exists()


@pytest.mark.django_db
def test_update_department(api_client, manager_user, manager_employee, engineering_department):
    department = engineering_department

    department.manager = manager_employee
    department.save()

    api_client.force_authenticate(user=manager_user)

    url = reverse("department-detail", kwargs={"pk": department.id})

    data = {
        "name": "Updated Engineering",
        "description": "Updated Engineering Department",
        "manager": manager_employee.id,
    }

    response = api_client.put(url, data, format="json")

    assert response.status_code == 200
    assert response.data["name"] == "Updated Engineering"

    department.refresh_from_db()

    assert department.name == "Updated Engineering"
    assert department.description == "Updated Engineering Department"


@pytest.mark.django_db
def test_delete_department(api_client, manager_user, manager_employee, engineering_department):
    department = engineering_department

    department.manager = manager_employee
    department.save()

    api_client.force_authenticate(user=manager_user)

    url = reverse("department-detail", kwargs={"pk": department.id})

    response = api_client.delete(url)

    assert response.status_code == 409
    assert response.data["detail"] == (
        "Cannot delete department because employees are assigned to it."
    )
    assert Department.objects.filter(pk=department.pk).exists()

import pytest
from django.urls import reverse

from operations.models import Operation


@pytest.mark.django_db
def test_admin_can_create_operation(admin_client, engineering_department, employee):
    data = {
        "title": "Admin Operation",
        "description": "Created by admin.",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.PENDING,
    }

    response = admin_client.post(reverse("operation-list"), data, format="json")

    assert response.status_code == 201


@pytest.mark.django_db
def test_manager_can_create_operation(manager_client, engineering_department, manager_employee):
    data = {
        "title": "Manager Operation",
        "description": "Created by manager.",
        "department": engineering_department.id,
        "assigned_to": manager_employee.id,
        "status": Operation.PENDING,
    }

    response = manager_client.post(reverse("operation-list"), data, format="json")

    assert response.status_code == 201


@pytest.mark.django_db
def test_employee_cannot_create_operation(authenticated_client, engineering_department, employee):
    data = {
        "title": "Employee Operation",
        "description": "Employee should not create this.",
        "department": engineering_department.id,
        "assigned_to": employee.id,
        "status": Operation.PENDING, 
    }

    response = authenticated_client.post(reverse("operation-list"), data, format="json")

    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_update_any_operation(admin_client, operation):
    response = admin_client.patch(reverse("operation-detail", kwargs={"pk": operation.pk}), {"title": "Admin Updated Operation"}, format="json")

    assert response.status_code == 200


@pytest.mark.django_db
def test_manager_can_update_own_department_operation(manager_client, manager_employee, engineering_department):
    operation = Operation.objects.create(
        title="Engineering Operation",
        description="Engineerring Task",
        department=engineering_department,
        assigned_to=manager_employee,
        status=Operation.PENDING,
    )   

    response = manager_client.patch(reverse("operation-detail", kwargs={"pk": operation.pk}), {"title": "Updated Engineering Operation"}, format="json")

    assert response.status_code == 200


@pytest.mark.django_db
def test_manager_cannot_update_another_department_operation(manager_client, finance_operation):
    response = manager_client.patch(reverse("operation-detail", kwargs={"pk": finance_operation.pk}), {"title": "Unauthorized Update"}, format="json")

    assert response.status_code == 403


@pytest.mark.django_db
def test_employee_cannot_update_operation(authenticated_client, operation):
    response = authenticated_client.patch(reverse("operation-detail", kwargs={"pk": operation.pk}), {"title": "Employee Update"}, format="json")

    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_delete_operation(admin_client, operation):
    response = admin_client.delete(reverse("operation-detail", kwargs={"pk": operation.pk}))

    assert response.status_code == 204


@pytest.mark.django_db
def test_manager_cannot_delete_operation(manager_client, operation):
    response = manager_client.delete(reverse("operation-detail", kwargs={"pk": operation.pk}))

    assert response.status_code == 403


@pytest.mark.django_db
def test_employee_cannot_delete_operation(authenticated_client, operation):
    response = authenticated_client.delete(reverse("operation-detail", kwargs={"pk": operation.pk}))

    assert response.status_code == 403

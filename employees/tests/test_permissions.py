import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


User = get_user_model()


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_employee_detail(employee):
    client = APIClient()
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = client.get(url)

    assert response.status_code == 401


@pytest.mark.django_db
def test_employee_owner_can_access_own_employee(authenticated_client, employee):
    authenticated_client.force_authenticate(user=employee.user)
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = authenticated_client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_employee_cannot_access_another_employee(authenticated_client,employee):
    other_user = User.objects.create_user(
        username="other",
        email="other@example.com",
        password="password123",
        first_name="Other",
        last_name="User",
    )
    authenticated_client.force_authenticate(user=other_user)
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = authenticated_client.get(url)

    assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_access_employee(admin_client, employee):    
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = admin_client.get(url)

    assert response.status_code == 200

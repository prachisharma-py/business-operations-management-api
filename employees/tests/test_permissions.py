import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_employee_detail(employee):
    client = APIClient()
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = client.get(url)

    assert response.status_code == 401


@pytest.mark.django_db
def test_employee_owner_can_access_own_employee(api_client, employee):
    api_client.force_authenticate(user=employee.user)
    url = reverse("employee-detail", kwargs={"pk": employee.pk})
    response = api_client.get(url)

    assert response.status_code == 200


    

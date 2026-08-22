import pytest

from django.urls import reverse
from departments.models import Department


@pytest.mark.django_db
def test_manager_cannot_modigy_another_managers_department(api_client, manager_user, second_manger_employee):
    department = Department.objects.create(
        name="Finance",
        description="Finance Department",
        manager=second_manger_employee,
    )

    api_client.force_authenticate(user=manager_user)

    url = reverse("department-detail", kwargs={"pk": department.id})

    response = api_client.patch(
        url,
        {
            "name": "Hacked Fianace",
            "description": "Should not be allowed",
            "manager": second_manger_employee.id,
        },
        format="json",
    )

    assert response.status_code == 403

    department.refresh_from_db()

    assert department.name == "Finance"

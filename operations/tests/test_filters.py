import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_filter_operations_by_department(authenticated_client, operation, finance_operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"department": operation.department.id})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_filter_operations_by_status(authenticated_client, operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"status": operation.status})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_filter_operations_by_assigned_to(authenticated_client, operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"assigned_to": operation.assigned_to.id})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_search_operations_by_title(authenticated_client, operation, finance_operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"search": "Server"})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Server Maintenance"


@pytest.mark.django_db
def test_search_operations_by_description(authenticated_client, operation, finance_operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"search": "monthly  finance"})

    assert response.status_code == 200
    assert response.data["count"] == 1
    assert len(response.data["results"]) == 1
    assert response.data["results"][0]["title"] == "Finance Report" 


@pytest.mark.django_db
def test_order_operations_by_title(authenticated_client, operation, finance_operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"ordering": "title"})

    assert response.status_code == 200

    title = [item["title"] for item in response.data["results"]]
    assert title == ["Finance Report", "Server Maintenance"]


@pytest.mark.django_db
def test_order_operations_by_created_at_descending(authenticated_client, operation, finance_operation):
    url = reverse("operation-list")

    response = authenticated_client.get(url, {"ordering": "-created_at"})

    assert response.status_code == 200

    title = [item["title"] for item in response.data["results"]]
    assert title == ["Finance Report", "Server Maintenance"]    

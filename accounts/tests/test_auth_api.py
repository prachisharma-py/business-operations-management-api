import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse("register")

    data = {
        "username": "alex",
        "email": "alex@example.com",
        "password": "StrongPass@123",
        "confirm_password": "StrongPass@123",
        "first_name": "Alex",
        "last_name": "Johnson",
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == 201


@pytest.mark.django_db
def test_login_success(api_client, user):
    url = reverse("login")

    response = api_client.post(
        url,
        {
            "username": "alex",
            "password": "password123",
        },
        format="json",
    )
    print(response.data)

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_invalid_credentials(api_client, user):
    url = reverse("login")

    response = api_client.post(
        url,
        {
            "email": "alex@example.com",
            "password": "wrongpassword",
        },
        format="json",
    )

    assert response.status_code == 400


@pytest.mark.django_db
def test_me_endpoint(api_client, user):
    api_client.force_authenticate(user=user)

    url = reverse("me")

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["email"] == user.email

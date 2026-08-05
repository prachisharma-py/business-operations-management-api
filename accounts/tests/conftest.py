import pytest

from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username="alex",
        email="alex@example.com",
        password="password123",
        first_name="Alex",
        last_name="Johnson",
    )

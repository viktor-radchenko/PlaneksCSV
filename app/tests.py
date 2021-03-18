import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model


def test_endpoints(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert b"Hello, world!" in response.content

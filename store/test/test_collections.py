from rest_framework import status
from rest_framework.test import APIClient
import pytest



# AAA (Arrange, Act, Assert)
@pytest.mark.django_db
class TestCreateCollection:

    def test_if_user_anonymous_returns_401(self):
        # Arrange
        client = APIClient()

        # Act
        response = client.post('/store/collections/', {'title': 'a'})

        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED





from django.contrib.auth.models import User
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

        def test_if_data_is_invalid_returns_401(self):
   
            client = APIClient()
            client.force_authentication(user = User(is_staff=True))
            response = client.post('/store/collections/', {'title': ''})
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            assert response.data['title'] is not None

       





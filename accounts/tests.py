from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from catalog import views, models

email = 'myemail@test.com'
password = 'password'


def create_super_user(**kwargs):
    defaults = {}
    defaults["email"] = email
    defaults["password"] = password
    defaults.update(**kwargs)
    return get_user_model().objects.create_superuser(**defaults)


def get_super_user(**kwargs):
    user = get_user_model().objects.get(email=email)
    return user


class AccountTests(APITestCase):
    user = get_user_model()
    client = APIClient()
    url = reverse('catalog_brand_list')

    def setUp(self):
        self.user = create_super_user()
        self.client = APIClient()

    def test_login(self):
        login = self.client.login(username=email, password=password)
        self.assertEqual(login, True)

    def force_authentication(self):
        self.client.force_authenticate(self.user)

    def test_list_brand(self):
        self.force_authentication()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_brand(self):
        data = {'name': 'new_brand'}
        self.force_authentication()
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Brand.objects.count(), 1)
        self.assertEqual(models.Brand.objects.get().name, 'new_brand')

    def test_create_brand_forbidden(self):
        data = {'name': 'new_brand'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

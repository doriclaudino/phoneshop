import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Brand, Model, Product
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_brand(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Brand.objects.create(**defaults)


def create_model(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Model.objects.create(**defaults)


def create_product(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "brand" not in defaults:
        defaults["brand"] = create_brand()
    return Product.objects.create(**defaults)


class BrandViewTest(unittest.TestCase):
    '''
    Tests for Brand
    '''

    def setUp(self):
        self.client = Client()

    def test_list_brand(self):
        url = reverse('catalog_brand_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_brand(self):
        url = reverse('catalog_brand_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_brand(self):
        brand = create_brand()
        url = reverse('catalog_brand_detail', args=[brand.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_brand(self):
        brand = create_brand()
        data = {
            "name": "name",
        }
        url = reverse('catalog_brand_update', args=[brand.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ModelViewTest(unittest.TestCase):
    '''
    Tests for Model
    '''

    def setUp(self):
        self.client = Client()

    def test_list_model(self):
        url = reverse('catalog_model_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_model(self):
        url = reverse('catalog_model_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_model(self):
        model = create_model()
        url = reverse('catalog_model_detail', args=[model.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_model(self):
        model = create_model()
        data = {
            "name": "name",
        }
        url = reverse('catalog_model_update', args=[model.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProductViewTest(unittest.TestCase):
    '''
    Tests for Product
    '''

    def setUp(self):
        self.client = Client()

    def test_list_product(self):
        url = reverse('catalog_product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        url = reverse('catalog_product_create')
        data = {
            "name": "name",
            "brand": create_brand().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_product(self):
        product = create_product()
        url = reverse('catalog_product_detail', args=[product.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = create_product()
        data = {
            "name": "name",
            "brand": create_brand().pk,
        }
        url = reverse('catalog_product_update', args=[product.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

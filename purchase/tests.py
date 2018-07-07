import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Supplier
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


def create_supplier(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["website"] = "website"
    defaults.update(**kwargs)
    return Supplier.objects.create(**defaults)


class SupplierViewTest(unittest.TestCase):
    '''
    Tests for Supplier
    '''
    def setUp(self):
        self.client = Client()

    def test_list_supplier(self):
        url = reverse('purchase_supplier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_supplier(self):
        url = reverse('purchase_supplier_create')
        data = {
            "name": "name",
            "website": "website",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_supplier(self):
        supplier = create_supplier()
        url = reverse('purchase_supplier_detail', args=[supplier.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_supplier(self):
        supplier = create_supplier()
        data = {
            "name": "name",
            "website": "website",
        }
        url = reverse('purchase_supplier_update', args=[supplier.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)



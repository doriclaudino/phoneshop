import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import IdentifierType, LocalType, Local, Identifier, Item
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from purchase.tests import create_purchaseorderitem


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


def create_identifiertype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return IdentifierType.objects.create(**defaults)


def create_localtype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return LocalType.objects.create(**defaults)


def create_local(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "type" not in defaults:
        defaults["type"] = create_localtype()
    return Local.objects.create(**defaults)


def create_identifier(**kwargs):
    defaults = {}
    defaults["value"] = "value"
    defaults.update(**kwargs)
    if "type" not in defaults:
        defaults["type"] = create_identifiertype()
    return Identifier.objects.create(**defaults)


def create_item(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "identifier" not in defaults:
        defaults["identifier"] = create_identifier()
    if "product" not in defaults:
        defaults["product"] = create_purchaseorderitem()
    if "local" not in defaults:
        defaults["local"] = create_local()
    return Item.objects.create(**defaults)


class IdentifierTypeViewTest(unittest.TestCase):
    '''
    Tests for IdentifierType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_identifiertype(self):
        url = reverse('inventory_identifiertype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_identifiertype(self):
        url = reverse('inventory_identifiertype_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_identifiertype(self):
        identifiertype = create_identifiertype()
        url = reverse('inventory_identifiertype_detail',
                      args=[identifiertype.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_identifiertype(self):
        identifiertype = create_identifiertype()
        data = {
            "name": "name",
        }
        url = reverse('inventory_identifiertype_update',
                      args=[identifiertype.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocalTypeViewTest(unittest.TestCase):
    '''
    Tests for LocalType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_localtype(self):
        url = reverse('inventory_localtype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_localtype(self):
        url = reverse('inventory_localtype_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_localtype(self):
        localtype = create_localtype()
        url = reverse('inventory_localtype_detail', args=[localtype.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_localtype(self):
        localtype = create_localtype()
        data = {
            "name": "name",
        }
        url = reverse('inventory_localtype_update', args=[localtype.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocalViewTest(unittest.TestCase):
    '''
    Tests for Local
    '''

    def setUp(self):
        self.client = Client()

    def test_list_local(self):
        url = reverse('inventory_local_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_local(self):
        url = reverse('inventory_local_create')
        data = {
            "name": "name",
            "type": create_localtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_local(self):
        local = create_local()
        url = reverse('inventory_local_detail', args=[local.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_local(self):
        local = create_local()
        data = {
            "name": "name",
            "type": create_localtype().pk,
        }
        url = reverse('inventory_local_update', args=[local.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class IdentifierViewTest(unittest.TestCase):
    '''
    Tests for Identifier
    '''

    def setUp(self):
        self.client = Client()

    def test_list_identifier(self):
        url = reverse('inventory_identifier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_identifier(self):
        url = reverse('inventory_identifier_create')
        data = {
            "value": "value",
            "type": create_identifiertype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_identifier(self):
        identifier = create_identifier()
        url = reverse('inventory_identifier_detail', args=[identifier.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_identifier(self):
        identifier = create_identifier()
        data = {
            "value": "value",
            "type": create_identifiertype().pk,
        }
        url = reverse('inventory_identifier_update', args=[identifier.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItemViewTest(unittest.TestCase):
    '''
    Tests for Item
    '''

    def setUp(self):
        self.client = Client()

    def test_list_item(self):
        url = reverse('inventory_item_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        url = reverse('inventory_item_create')
        data = {
            "identifier": create_identifier().pk,
            "product": create_purchaseorderitem().pk,
            "local": create_local().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_item(self):
        item = create_item()
        url = reverse('inventory_item_detail', args=[item.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_item(self):
        item = create_item()
        data = {
            "identifier": create_identifier().pk,
            "product": create_purchaseorderitem().pk,
            "local": create_local().pk,
        }
        url = reverse('inventory_item_update', args=[item.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

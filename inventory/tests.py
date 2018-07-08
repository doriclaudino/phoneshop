import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import IdentifierType, LocationType, Location, Identifier, Item
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


def create_locationtype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return LocationType.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "type" not in defaults:
        defaults["type"] = create_locationtype()
    return Location.objects.create(**defaults)


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
    if "location" not in defaults:
        defaults["location"] = create_location()
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


class LocationTypeViewTest(unittest.TestCase):
    '''
    Tests for LocationType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_locationtype(self):
        url = reverse('inventory_locationtype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_locationtype(self):
        url = reverse('inventory_locationtype_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_locationtype(self):
        locationtype = create_locationtype()
        url = reverse('inventory_locationtype_detail',
                      args=[locationtype.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_locationtype(self):
        locationtype = create_locationtype()
        data = {
            "name": "name",
        }
        url = reverse('inventory_locationtype_update',
                      args=[locationtype.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''

    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('inventory_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('inventory_location_create')
        data = {
            "name": "name",
            "type": create_locationtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('inventory_location_detail', args=[location.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "name": "name",
            "type": create_locationtype().pk,
        }
        url = reverse('inventory_location_update', args=[location.slug, ])
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
            "location": create_location().pk,
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
            "location": create_location().pk,
        }
        url = reverse('inventory_item_update', args=[item.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

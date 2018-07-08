import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Seller, SellOrderStatus, SellOrder, SellOrderItem
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from logistic.tests import create_tracking
from catalog.tests import create_productmodel


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


def create_seller(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["website"] = "website"
    defaults.update(**kwargs)
    return Seller.objects.create(**defaults)


def create_sellorderstatus(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return SellOrderStatus.objects.create(**defaults)


def create_sellorder(**kwargs):
    defaults = {}
    defaults["details"] = "details"
    defaults.update(**kwargs)
    if "seller" not in defaults:
        defaults["seller"] = create_seller()
    if "status" not in defaults:
        defaults["status"] = create_sellorderstatus()
    if "tracking" not in defaults:
        defaults["tracking"] = create_tracking()
    return SellOrder.objects.create(**defaults)


def create_sellorderitem(**kwargs):
    defaults = {}
    defaults["quantity"] = 1
    defaults["price"] = 100.00
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_productmodel()
    if "order" not in defaults:
        defaults["order"] = create_sellorder()
    return SellOrderItem.objects.create(**defaults)


class SellerViewTest(unittest.TestCase):
    '''
    Tests for Seller
    '''

    def setUp(self):
        self.client = Client()

    def test_list_seller(self):
        url = reverse('sales_seller_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_seller(self):
        url = reverse('sales_seller_create')
        data = {
            "name": "name",
            "website": "website",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_seller(self):
        seller = create_seller()
        url = reverse('sales_seller_detail', args=[seller.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_seller(self):
        seller = create_seller()
        data = {
            "name": "name",
            "website": "website",
        }
        url = reverse('sales_seller_update', args=[seller.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SellOrderStatusViewTest(unittest.TestCase):
    '''
    Tests for SellOrderStatus
    '''

    def setUp(self):
        self.client = Client()

    def test_list_sellorderstatus(self):
        url = reverse('sales_sellorderstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sellorderstatus(self):
        url = reverse('sales_sellorderstatus_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sellorderstatus(self):
        sellorderstatus = create_sellorderstatus()
        url = reverse('sales_sellorderstatus_detail',
                      args=[sellorderstatus.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sellorderstatus(self):
        sellorderstatus = create_sellorderstatus()
        data = {
            "name": "name",
        }
        url = reverse('sales_sellorderstatus_update',
                      args=[sellorderstatus.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SellOrderViewTest(unittest.TestCase):
    '''
    Tests for SellOrder
    '''

    def setUp(self):
        self.client = Client()

    def test_list_sellorder(self):
        url = reverse('sales_sellorder_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sellorder(self):
        url = reverse('sales_sellorder_create')
        data = {
            "details": "details",
            "seller": create_seller().pk,
            "status": create_sellorderstatus().pk,
            "tracking": create_tracking().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sellorder(self):
        sellorder = create_sellorder()
        url = reverse('sales_sellorder_detail', args=[sellorder.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sellorder(self):
        sellorder = create_sellorder()
        data = {
            "details": "details",
            "seller": create_seller().pk,
            "status": create_sellorderstatus().pk,
            "tracking": create_tracking().pk,
        }
        url = reverse('sales_sellorder_update', args=[sellorder.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SellOrderItemViewTest(unittest.TestCase):
    '''
    Tests for SellOrderItem
    '''

    def setUp(self):
        self.client = Client()

    def test_list_sellorderitem(self):
        url = reverse('sales_sellorderitem_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sellorderitem(self):
        url = reverse('sales_sellorderitem_create')
        data = {
            "quantity": 1,
            "price": 100.00,
            "product": create_productmodel().pk,
            "order": create_sellorder().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sellorderitem(self):
        sellorderitem = create_sellorderitem()
        url = reverse('sales_sellorderitem_detail',
                      args=[sellorderitem.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sellorderitem(self):
        sellorderitem = create_sellorderitem()
        data = {
            "quantity": 1,
            "price": 100.00,
            "product": create_productmodel().pk,
            "order": create_sellorder().pk,
        }
        url = reverse('sales_sellorderitem_update',
                      args=[sellorderitem.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

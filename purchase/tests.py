import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Supplier, PurchaseOrderStatus, PurchaseOrder, PurchaseOrderItem
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


def create_supplier(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["website"] = "website"
    defaults.update(**kwargs)
    return Supplier.objects.create(**defaults)


def create_purchaseorderstatus(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return PurchaseOrderStatus.objects.create(**defaults)


def create_purchaseorder(**kwargs):
    defaults = {}
    defaults["details"] = "details"
    defaults.update(**kwargs)
    if "supplier" not in defaults:
        defaults["supplier"] = create_supplier()
    if "status" not in defaults:
        defaults["status"] = create_purchaseorderstatus()
    if "tracking" not in defaults:
        defaults["tracking"] = create_tracking()
    return PurchaseOrder.objects.create(**defaults)


def create_purchaseorderitem(**kwargs):
    defaults = {}
    defaults["quantity"] = 1
    defaults["price"] = 10.00
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_productmodel()
    if "order" not in defaults:
        defaults["order"] = create_purchaseorder()
    return PurchaseOrderItem.objects.create(**defaults)


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
        url = reverse('purchase_supplier_detail', args=[supplier.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_supplier(self):
        supplier = create_supplier()
        data = {
            "name": "name",
            "website": "website",
        }
        url = reverse('purchase_supplier_update', args=[supplier.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchaseOrderStatusViewTest(unittest.TestCase):
    '''
    Tests for PurchaseOrderStatus
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchaseorderstatus(self):
        url = reverse('purchase_purchaseorderstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchaseorderstatus(self):
        url = reverse('purchase_purchaseorderstatus_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchaseorderstatus(self):
        purchaseorderstatus = create_purchaseorderstatus()
        url = reverse('purchase_purchaseorderstatus_detail',
                      args=[purchaseorderstatus.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchaseorderstatus(self):
        purchaseorderstatus = create_purchaseorderstatus()
        data = {
            "name": "name",
        }
        url = reverse('purchase_purchaseorderstatus_update',
                      args=[purchaseorderstatus.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchaseOrderViewTest(unittest.TestCase):
    '''
    Tests for PurchaseOrder
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchaseorder(self):
        url = reverse('purchase_purchaseorder_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchaseorder(self):
        url = reverse('purchase_purchaseorder_create')
        data = {
            "details": "details",
            "supplier": create_supplier().pk,
            "status": create_purchaseorderstatus().pk,
            "tracking": create_tracking().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchaseorder(self):
        purchaseorder = create_purchaseorder()
        url = reverse('purchase_purchaseorder_detail',
                      args=[purchaseorder.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchaseorder(self):
        purchaseorder = create_purchaseorder()
        data = {
            "details": "details",
            "supplier": create_supplier().pk,
            "status": create_purchaseorderstatus().pk,
            "tracking": create_tracking().pk,
        }
        url = reverse('purchase_purchaseorder_update',
                      args=[purchaseorder.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchaseOrderItemViewTest(unittest.TestCase):
    '''
    Tests for PurchaseOrderItem
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchaseorderitem(self):
        url = reverse('purchase_purchaseorderitem_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchaseorderitem(self):
        url = reverse('purchase_purchaseorderitem_create')
        data = {
            "quantity": 1,
            "price": 10.00,
            "product": create_supplier().pk,
            "order": create_purchaseorder().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchaseorderitem(self):
        purchaseorderitem = create_purchaseorderitem()
        url = reverse('purchase_purchaseorderitem_detail',
                      args=[purchaseorderitem.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchaseorderitem(self):
        purchaseorderitem = create_purchaseorderitem()
        data = {
            "quantity": 1,
            "price": 10.00,
            "product": create_supplier().pk,
            "order": create_purchaseorder().pk,
        }
        url = reverse('purchase_purchaseorderitem_update',
                      args=[purchaseorderitem.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

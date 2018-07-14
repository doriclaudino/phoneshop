import unittest
import uuid
from django.core.urlresolvers import reverse
from django.test import Client
from .models import CostType, PurchaseCost, ItemCost, SellCost, TrackingCost
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from sales.tests import create_sellorder
from purchase.tests import create_purchaseorder
from inventory.tests import create_item
from payments.tests import create_payment
from logistic.tests import create_tracking


def create_costtype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    return CostType.objects.create(**defaults)


def create_purchasecost(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    if "ref" not in defaults:
        defaults["ref"] = create_purchaseorder()
    if "type" not in defaults:
        defaults["type"] = create_costtype()
    return PurchaseCost.objects.create(**defaults)


def create_itemcost(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    if "ref" not in defaults:
        defaults["ref"] = create_item()
    if "type" not in defaults:
        defaults["type"] = create_costtype()
    return ItemCost.objects.create(**defaults)


def create_sellcost(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    if "ref" not in defaults:
        defaults["ref"] = create_sellorder()
    if "type" not in defaults:
        defaults["type"] = create_costtype()
    return SellCost.objects.create(**defaults)


def create_trackingcost(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    if "ref" not in defaults:
        defaults["ref"] = create_tracking()
    if "type" not in defaults:
        defaults["type"] = create_costtype()
    return TrackingCost.objects.create(**defaults)


class CostTypeViewTest(unittest.TestCase):
    '''
    Tests for CostType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_costtype(self):
        url = reverse('costs_costtype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_costtype(self):
        url = reverse('costs_costtype_create')
        data = {
            "name": "name",
            "slug": "slug",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_costtype(self):
        costtype = create_costtype()
        url = reverse('costs_costtype_detail', args=[costtype.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_costtype(self):
        costtype = create_costtype()
        data = {
            "name": uuid.uuid4(),
            "slug": "slug",
        }
        url = reverse('costs_costtype_update', args=[costtype.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchaseCostViewTest(unittest.TestCase):
    '''
    Tests for PurchaseCost
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchasecost(self):
        url = reverse('costs_purchasecost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchasecost(self):
        url = reverse('costs_purchasecost_create')
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_purchaseorder().pk,
            "type": create_costtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchasecost(self):
        purchasecost = create_purchasecost()
        url = reverse('costs_purchasecost_detail', args=[purchasecost.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchasecost(self):
        purchasecost = create_purchasecost()
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_purchaseorder().pk,
            "type": create_costtype().pk,
        }
        url = reverse('costs_purchasecost_update', args=[purchasecost.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItemCostViewTest(unittest.TestCase):
    '''
    Tests for ItemCost
    '''

    def setUp(self):
        self.client = Client()

    def test_list_itemcost(self):
        url = reverse('costs_itemcost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_itemcost(self):
        url = reverse('costs_itemcost_create')
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_item().pk,
            "type": create_costtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_itemcost(self):
        itemcost = create_itemcost()
        url = reverse('costs_itemcost_detail', args=[itemcost.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_itemcost(self):
        itemcost = create_itemcost()
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_item().pk,
            "type": create_costtype().pk,
        }
        url = reverse('costs_itemcost_update', args=[itemcost.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SellCostViewTest(unittest.TestCase):
    '''
    Tests for SellCost
    '''

    def setUp(self):
        self.client = Client()

    def test_list_sellcost(self):
        url = reverse('costs_sellcost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sellcost(self):
        url = reverse('costs_sellcost_create')
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_sellorder().pk,
            "type": create_costtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sellcost(self):
        sellcost = create_sellcost()
        url = reverse('costs_sellcost_detail', args=[sellcost.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sellcost(self):
        sellcost = create_sellcost()
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_sellorder().pk,
            "type": create_costtype().pk,
        }
        url = reverse('costs_sellcost_update', args=[sellcost.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrackingCostViewTest(unittest.TestCase):
    '''
    Tests for TrackingCost
    '''

    def setUp(self):
        self.client = Client()

    def test_list_trackingcost(self):
        url = reverse('costs_trackingcost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_trackingcost(self):
        url = reverse('costs_trackingcost_create')
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_tracking().pk,
            "type": create_costtype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_trackingcost(self):
        trackingcost = create_trackingcost()
        url = reverse('costs_trackingcost_detail', args=[trackingcost.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_trackingcost(self):
        trackingcost = create_trackingcost()
        data = {
            "slug": "slug",
            "payment": create_payment().pk,
            "ref": create_tracking().pk,
            "type": create_costtype().pk,
        }
        url = reverse('costs_trackingcost_update', args=[trackingcost.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

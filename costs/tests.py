import unittest
import uuid
from django.core.urlresolvers import reverse
from django.test import Client
from .models import CostType, Cost, PurchaseCosts, SellCosts, ItemCosts
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from sales.tests import create_sellorder
from purchase.tests import create_purchaseorder
from inventory.tests import create_item
from payments.tests import create_payment


def create_costtype(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return CostType.objects.create(**defaults)


def create_cost(**kwargs):
    defaults = {}
    defaults["details"] = "details"
    defaults.update(**kwargs)
    if "type" not in defaults:
        defaults["type"] = create_costtype()
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    return Cost.objects.create(**defaults)


def create_purchasecosts(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "ref" not in defaults:
        defaults["ref"] = create_purchaseorder()
    if "cost" not in defaults:
        defaults["cost"] = create_cost()
    return PurchaseCosts.objects.create(**defaults)


def create_sellcosts(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "ref" not in defaults:
        defaults["ref"] = create_sellorder()
    if "cost" not in defaults:
        defaults["cost"] = create_cost()
    return SellCosts.objects.create(**defaults)


def create_itemcosts(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "ref" not in defaults:
        defaults["ref"] = create_item()
    if "cost" not in defaults:
        defaults["cost"] = create_cost()
    return ItemCosts.objects.create(**defaults)


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
        }
        url = reverse('costs_costtype_update', args=[costtype.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CostViewTest(unittest.TestCase):
    '''
    Tests for Cost
    '''

    def setUp(self):
        self.client = Client()

    def test_list_cost(self):
        url = reverse('costs_cost_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_cost(self):
        url = reverse('costs_cost_create')
        data = {
            "details": "details",
            "type": create_costtype().pk,
            "payment": create_payment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_cost(self):
        cost = create_cost()
        url = reverse('costs_cost_detail', args=[cost.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_cost(self):
        cost = create_cost()
        data = {
            "details": "details",
            "type": create_costtype().pk,
            "payment": create_payment().pk,
        }
        url = reverse('costs_cost_update', args=[cost.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchaseCostsViewTest(unittest.TestCase):
    '''
    Tests for PurchaseCosts
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchasecosts(self):
        url = reverse('costs_purchasecosts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchasecosts(self):
        url = reverse('costs_purchasecosts_create')
        data = {
            "ref": create_purchaseorder().pk,
            "cost": create_cost().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchasecosts(self):
        purchasecosts = create_purchasecosts()
        url = reverse('costs_purchasecosts_detail',
                      args=[purchasecosts.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchasecosts(self):
        purchasecosts = create_purchasecosts()
        data = {
            "ref": create_purchaseorder().pk,
            "cost": create_cost().pk,
        }
        url = reverse('costs_purchasecosts_update',
                      args=[purchasecosts.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SellCostsViewTest(unittest.TestCase):
    '''
    Tests for SellCosts
    '''

    def setUp(self):
        self.client = Client()

    def test_list_sellcosts(self):
        url = reverse('costs_sellcosts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_sellcosts(self):
        url = reverse('costs_sellcosts_create')
        data = {
            "ref": create_sellorder().pk,
            "cost": create_cost().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_sellcosts(self):
        sellcosts = create_sellcosts()
        url = reverse('costs_sellcosts_detail', args=[sellcosts.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_sellcosts(self):
        sellcosts = create_sellcosts()
        data = {
            "ref": create_sellorder().pk,
            "cost": create_cost().pk,
        }
        url = reverse('costs_sellcosts_update', args=[sellcosts.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ItemCostsViewTest(unittest.TestCase):
    '''
    Tests for ItemCosts
    '''

    def setUp(self):
        self.client = Client()

    def test_list_itemcosts(self):
        url = reverse('costs_itemcosts_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_itemcosts(self):
        url = reverse('costs_itemcosts_create')
        data = {
            "ref": create_item().pk,
            "cost": create_cost().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_itemcosts(self):
        itemcosts = create_itemcosts()
        url = reverse('costs_itemcosts_detail', args=[itemcosts.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_itemcosts(self):
        itemcosts = create_itemcosts()
        data = {
            "ref": create_item().pk,
            "cost": create_cost().pk,
        }
        url = reverse('costs_itemcosts_update', args=[itemcosts.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

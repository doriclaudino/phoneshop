import unittest
import uuid
from django.core.urlresolvers import reverse
from django.test import Client
from .models import PaymentMethod, PaymentStatus, SalePayment, PurchasePayment, TrackingPayment
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from sales.tests import create_sellorder
from purchase.tests import create_purchaseorder
from logistic.tests import create_tracking
from django.utils import timezone


def create_paymentmethod(**kwargs):
    defaults = {}
    defaults["name"] = uuid.uuid4()
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    return PaymentMethod.objects.create(**defaults)


def create_paymentstatus(**kwargs):
    defaults = {}
    defaults["name"] = uuid.uuid4()
    defaults["slug"] = "slug"
    defaults.update(**kwargs)
    return PaymentStatus.objects.create(**defaults)


def create_salepayment(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["date"] = timezone.now()
    defaults["amount"] = 100.00
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_paymentstatus()
    if "method" not in defaults:
        defaults["method"] = create_paymentmethod()
    if "ref" not in defaults:
        defaults["ref"] = create_sellorder()
    return SalePayment.objects.create(**defaults)


def create_purchasepayment(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["date"] = timezone.now()
    defaults["amount"] = 100.00
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_paymentstatus()
    if "method" not in defaults:
        defaults["method"] = create_paymentmethod()
    if "ref" not in defaults:
        defaults["ref"] = create_purchaseorder()
    return PurchasePayment.objects.create(**defaults)


def create_trackingpayment(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["date"] = timezone.now()
    defaults["amount"] = 100.00
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_paymentstatus()
    if "method" not in defaults:
        defaults["method"] = create_paymentmethod()
    if "ref" not in defaults:
        defaults["ref"] = create_tracking()
    return TrackingPayment.objects.create(**defaults)


class PaymentMethodViewTest(unittest.TestCase):
    '''
    Tests for PaymentMethod
    '''

    def setUp(self):
        self.client = Client()

    def test_list_paymentmethod(self):
        url = reverse('payments_paymentmethod_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_paymentmethod(self):
        url = reverse('payments_paymentmethod_create')
        data = {
            "name": uuid.uuid4(),
            "slug": "slug",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_paymentmethod(self):
        paymentmethod = create_paymentmethod()
        url = reverse('payments_paymentmethod_detail',
                      args=[paymentmethod.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_paymentmethod(self):
        paymentmethod = create_paymentmethod()
        data = {
            "name": uuid.uuid4(),
            "slug": "slug",
        }
        url = reverse('payments_paymentmethod_update',
                      args=[paymentmethod.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PaymentStatusViewTest(unittest.TestCase):
    '''
    Tests for PaymentStatus
    '''

    def setUp(self):
        self.client = Client()

    def test_list_paymentstatus(self):
        url = reverse('payments_paymentstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_paymentstatus(self):
        url = reverse('payments_paymentstatus_create')
        data = {
            "name": uuid.uuid4(),
            "slug": "slug",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_paymentstatus(self):
        paymentstatus = create_paymentstatus()
        url = reverse('payments_paymentstatus_detail',
                      args=[paymentstatus.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_paymentstatus(self):
        paymentstatus = create_paymentstatus()
        data = {
            "name": uuid.uuid4(),
        }
        url = reverse('payments_paymentstatus_update',
                      args=[paymentstatus.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class SalePaymentViewTest(unittest.TestCase):
    '''
    Tests for SalePayment
    '''

    def setUp(self):
        self.client = Client()

    def test_list_salepayment(self):
        url = reverse('payments_salepayment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_salepayment(self):
        url = reverse('payments_salepayment_create')
        data = {
            "slug": "slug",
            "date": timezone.now(),
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_paymentmethod().pk,
            "ref": create_sellorder().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_salepayment(self):
        salepayment = create_salepayment()
        url = reverse('payments_salepayment_detail', args=[salepayment.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_salepayment(self):
        salepayment = create_salepayment()
        data = {
            "slug": "slug",
            "date": timezone.now(),
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_paymentmethod().pk,
            "ref": create_sellorder().pk,
        }
        url = reverse('payments_salepayment_update', args=[salepayment.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PurchasePaymentViewTest(unittest.TestCase):
    '''
    Tests for PurchasePayment
    '''

    def setUp(self):
        self.client = Client()

    def test_list_purchasepayment(self):
        url = reverse('payments_purchasepayment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_purchasepayment(self):
        url = reverse('payments_purchasepayment_create')
        data = {
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_purchaseorder().pk,
            "ref": create_purchaseorder().pk,
        }
        print(url)

        response = self.client.post(url, data=data)
        print(response)
        self.assertEqual(response.status_code, 302)

    def test_detail_purchasepayment(self):
        purchasepayment = create_purchasepayment()
        url = reverse('payments_purchasepayment_detail',
                      args=[purchasepayment.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_purchasepayment(self):
        purchasepayment = create_purchasepayment()
        data = {
            "slug": "slug",
            "date": timezone.now(),
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_paymentmethod().pk,
            "ref": create_purchaseorder().pk,
        }
        url = reverse('payments_purchasepayment_update',
                      args=[purchasepayment.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrackingPaymentViewTest(unittest.TestCase):
    '''
    Tests for TrackingPayment
    '''

    def setUp(self):
        self.client = Client()

    def test_list_trackingpayment(self):
        url = reverse('payments_trackingpayment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_trackingpayment(self):
        url = reverse('payments_trackingpayment_create')
        data = {
            "slug": "slug",
            "date": timezone.now(),
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_paymentmethod().pk,
            "ref": create_tracking().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_trackingpayment(self):
        trackingpayment = create_trackingpayment()
        url = reverse('payments_trackingpayment_detail',
                      args=[trackingpayment.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_trackingpayment(self):
        trackingpayment = create_trackingpayment()
        data = {
            "slug": "slug",
            "date": timezone.now(),
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "method": create_paymentmethod().pk,
            "ref": create_tracking().pk,
        }
        url = reverse('payments_trackingpayment_update',
                      args=[trackingpayment.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

import unittest
import uuid
from django.core.urlresolvers import reverse
from django.test import Client
from .models import PaymentType, PaymentStatus, Payment, OrderPayments
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from sales.tests import create_sellorder
from django.utils import timezone


def create_paymenttype(**kwargs):
    defaults = {}
    defaults["name"] = uuid.uuid4()
    defaults.update(**kwargs)
    return PaymentType.objects.create(**defaults)


def create_paymentstatus(**kwargs):
    defaults = {}
    defaults["name"] = uuid.uuid4()
    defaults.update(**kwargs)
    return PaymentStatus.objects.create(**defaults)


def create_payment(**kwargs):
    defaults = {}
    defaults["amount"] = 100.00
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_paymentstatus()
    if "type" not in defaults:
        defaults["type"] = create_paymenttype()
    return Payment.objects.create(**defaults)


def create_orderpayments(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "order" not in defaults:
        defaults["order"] = create_sellorder()
    if "payment" not in defaults:
        defaults["payment"] = create_payment()
    return OrderPayments.objects.create(**defaults)


class PaymentTypeViewTest(unittest.TestCase):
    '''
    Tests for PaymentType
    '''

    def setUp(self):
        self.client = Client()

    def test_list_paymenttype(self):
        url = reverse('payments_paymenttype_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_paymenttype(self):
        url = reverse('payments_paymenttype_create')
        data = {
            "name": uuid.uuid4(),
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_paymenttype(self):
        paymenttype = create_paymenttype()
        url = reverse('payments_paymenttype_detail', args=[paymenttype.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_paymenttype(self):
        paymenttype = create_paymenttype()
        data = {
            "name": uuid.uuid4(),
        }
        url = reverse('payments_paymenttype_update', args=[paymenttype.slug, ])
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
            "date": timezone.now,
            "name": uuid.uuid4(),
        }
        url = reverse('payments_paymentstatus_update',
                      args=[paymentstatus.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PaymentViewTest(unittest.TestCase):
    '''
    Tests for Payment
    '''

    def setUp(self):
        self.client = Client()

    def test_list_payment(self):
        url = reverse('payments_payment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_payment(self):
        url = reverse('payments_payment_create')
        data = {
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "type": create_paymenttype().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_payment(self):
        payment = create_payment()
        url = reverse('payments_payment_detail', args=[payment.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_payment(self):
        payment = create_payment()
        data = {
            "amount": 100.00,
            "status": create_paymentstatus().pk,
            "type": create_paymenttype().pk,
        }
        url = reverse('payments_payment_update', args=[payment.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrderPaymentsViewTest(unittest.TestCase):
    '''
    Tests for OrderPayments
    '''

    def setUp(self):
        self.client = Client()

    def test_list_orderpayments(self):
        url = reverse('payments_orderpayments_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_orderpayments(self):
        url = reverse('payments_orderpayments_create')
        data = {
            "order": create_sellorder().pk,
            "payment": create_payment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_orderpayments(self):
        orderpayments = create_orderpayments()
        url = reverse('payments_orderpayments_detail',
                      args=[orderpayments.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_orderpayments(self):
        orderpayments = create_orderpayments()
        data = {
            "order": create_sellorder().pk,
            "payment": create_payment().pk,
        }
        url = reverse('payments_orderpayments_update',
                      args=[orderpayments.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Location, Carrier, TrackingStatus, Tracking
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


def create_django_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_location(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Location.objects.create(**defaults)


def create_carrier(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["website"] = "website"
    defaults["tracking_url"] = "tracking_url"
    defaults.update(**kwargs)
    return Carrier.objects.create(**defaults)


def create_trackingstatus(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return TrackingStatus.objects.create(**defaults)


def create_tracking(**kwargs):
    defaults = {}
    defaults["number"] = "number"
    defaults["description"] = "description"
    defaults["previous"] = None
    defaults.update(**kwargs)
    if "status" not in defaults:
        defaults["status"] = create_trackingstatus()
    if "previous" not in defaults:
        defaults["previous"] = create_tracking()
    if "carrier" not in defaults:
        defaults["carrier"] = create_carrier()
    return Tracking.objects.create(**defaults)


class LocationViewTest(unittest.TestCase):
    '''
    Tests for Location
    '''

    def setUp(self):
        self.client = Client()

    def test_list_location(self):
        url = reverse('logistic_location_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_location(self):
        url = reverse('logistic_location_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_location(self):
        location = create_location()
        url = reverse('logistic_location_detail', args=[location.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_location(self):
        location = create_location()
        data = {
            "name": "name",
        }
        url = reverse('logistic_location_update', args=[location.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CarrierViewTest(unittest.TestCase):
    '''
    Tests for Carrier
    '''

    def setUp(self):
        self.client = Client()

    def test_list_carrier(self):
        url = reverse('logistic_carrier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_carrier(self):
        url = reverse('logistic_carrier_create')
        data = {
            "name": "name",
            "website": "website",
            "tracking_url": "tracking_url",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_carrier(self):
        carrier = create_carrier()
        url = reverse('logistic_carrier_detail', args=[carrier.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_carrier(self):
        carrier = create_carrier()
        data = {
            "name": "name",
            "website": "website",
            "tracking_url": "tracking_url",
        }
        url = reverse('logistic_carrier_update', args=[carrier.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrackingStatusViewTest(unittest.TestCase):
    '''
    Tests for TrackingStatus
    '''

    def setUp(self):
        self.client = Client()

    def test_list_trackingstatus(self):
        url = reverse('logistic_trackingstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_trackingstatus(self):
        url = reverse('logistic_trackingstatus_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_trackingstatus(self):
        trackingstatus = create_trackingstatus()
        url = reverse('logistic_trackingstatus_detail',
                      args=[trackingstatus.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_trackingstatus(self):
        trackingstatus = create_trackingstatus()
        data = {
            "name": "name",
        }
        url = reverse('logistic_trackingstatus_update',
                      args=[trackingstatus.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TrackingViewTest(unittest.TestCase):
    '''
    Tests for Tracking
    '''

    def setUp(self):
        self.client = Client()

    def test_list_tracking(self):
        url = reverse('logistic_tracking_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_tracking(self):
        url = reverse('logistic_tracking_create')
        data = {
            "number": "number",
            "description": "description",
            "status": create_trackingstatus().pk,
            "previous": create_tracking().pk,
            "carrier": create_carrier().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_tracking(self):
        tracking = create_tracking()
        url = reverse('logistic_tracking_detail', args=[tracking.slug, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_tracking(self):
        tracking = create_tracking()
        data = {
            "number": "number",
            "description": "description",
            "status": create_trackingstatus().pk,
            "previous": create_tracking().pk,
            "carrier": create_carrier().pk,
        }
        url = reverse('logistic_tracking_update', args=[tracking.slug, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

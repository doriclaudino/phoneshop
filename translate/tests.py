from django.test import TestCase, SimpleTestCase, Client
from django.core.urlresolvers import reverse
from django.utils import translation
from .views import testView
from django.template import Template, Context

# Create your tests here.


class TranslationTest(TestCase):
    '''
    Test for Translation using i18n
    '''

    def setUp(self):
        self.client = Client()

    def test_translate_append_default(self):
        url = reverse('logistic_location_list')
        self.assertEqual(url, "/en-us/logistic/location/")

    def test_translate_append_prefix(self):
        translation.activate('pt-br')
        url = reverse('logistic_location_list')
        self.assertEqual(url, "/pt-br/logistic/location/")

    def test_translate_to_pt_br(self):
        translation.activate('pt-br')
        self.assertEqual(translation.ugettext('Portuguese'),
                         'Portugues', 'i18n support should be activated.')

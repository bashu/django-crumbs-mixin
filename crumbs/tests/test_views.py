# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class CrumbsMixinTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'

    def test_context_data(self):
        response = self.client.get(reverse('test_view'))
        self.assertEqual(response.context['show_crumbs'], True)

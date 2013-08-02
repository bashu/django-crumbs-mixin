# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse


class CrumbsTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'
        self.old_MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
        middleware_class = 'breadcrumbs.middleware.BreadcrumbsMiddleware'
        if middleware_class not in settings.MIDDLEWARE_CLASSES:
            settings.MIDDLEWARE_CLASSES += (middleware_class,)

    def tearDown(self):
        settings.MIDDLEWARE_CLASSES = self.old_MIDDLEWARE_CLASSES

    def test_default(self):
        response = self.client.get(reverse('test_view'))
        self.failUnless(hasattr(response.context['request'], 'breadcrumbs'))

    def test_context_data(self):
        response = self.client.get(reverse('test_view'))
        self.assertEqual(response.context['show_crumbs'], True)


class NoCrumbsTest(TestCase):

    def setUp(self):
        self.base_url = 'http://testserver'

    def test_context_data(self):
        response = self.client.get(reverse('test_view'))
        self.assertEqual(response.context['show_crumbs'], False)

# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse


class CrumbsTest(TestCase):

    def setUp(self):
        self.view_url = reverse('test_view')

    def test_crumbs(self):
        response = self.client.get(self.view_url)
        self.failUnless(hasattr(response.context['request'], 'breadcrumbs'))

    def test_context_data(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.context['show_crumbs'], True)


class NoCrumbsTest(TestCase):

    def setUp(self):
        self.view_url = reverse('test_view')

        self.old_MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
        middleware_class = 'breadcrumbs.middleware.BreadcrumbsMiddleware'
        for x, m in enumerate(settings.MIDDLEWARE_CLASSES):
            if m.startswith(middleware_class):
                settings.MIDDLEWARE_CLASSES.pop(x)

    def tearDown(self):
        settings.MIDDLEWARE_CLASSES = self.old_MIDDLEWARE_CLASSES

    def test_context_data(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.context['show_crumbs'], False)

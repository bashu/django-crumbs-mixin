# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import RequestFactory
from django.template import loader, Context

from breadcrumbs.breadcrumbs import Breadcrumbs


class BreadcrumbsTest(TestCase):

    @property
    def tt(self):
        return loader.get_template_from_string("""{% load crumbs_tags %}{% breadcrumbs object %}""")

    def setUp(self):
        self.rf = RequestFactory()

    def test_crumbs(self):
        # prepare breadcumbs
        request = self.rf.get('/')
        request.breadcrumbs = Breadcrumbs((['Home', '/'], ['Test', '/test/']))

        response = self.tt.render(Context({'object': None, 'request': request}))
        self.assertTrue("Home / Test" in response)

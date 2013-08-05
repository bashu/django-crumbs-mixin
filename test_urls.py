# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns, url

from crumbs.views import CrumbsMixin


class TestView(CrumbsMixin, TemplateView):
    template_name = 'test.html'

    def get_crumbs(self, context):
        return [('Home', '/'), ('Test', '/test/')]

urlpatterns = patterns('',
    url(r'^test/', TestView.as_view(), name='test_view'),
)

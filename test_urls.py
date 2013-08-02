# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.conf.urls.defaults import patterns, url

from crumbs.views import CrumbsMixin


class TestView(CrumbsMixin, TemplateView):
    template_name = 'test_view.html'
    model = User

    def get_crumbs(self, context):
        return [('Home', '/'), ('View', reverse('test_view'))]

urlpatterns = patterns('',
    url(r'^test/', TestView.as_view(), name='test_view'),
)

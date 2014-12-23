# -*- coding: utf-8 -*-

import hashlib

from django.core.cache import cache
from django.utils.encoding import smart_str
from django.contrib.sites.models import get_current_site

from .conf import CACHE_PREFIX, CACHE_TIMEOUT


def make_cache_key(domain, path, cache_prefix=CACHE_PREFIX):
    return '%s:%s' % (cache_prefix, hashlib.md5(smart_str('%s%s' % (
        domain, path))).hexdigest())


class CrumbsMixin(object):

    def __init__(self, *args, **kwargs):
        super(CrumbsMixin, self).__init__(*args, **kwargs)
        if not hasattr(self, 'cache_timeout'):
            self.cache_timeout = CACHE_TIMEOUT

    def get_crumbs_cache_key(self):
        current_site = get_current_site(self.request)

        return make_cache_key(current_site.domain, self.request.get_full_path())

    def get_breadcrumbs(self, context):
        cache_key = self.get_crumbs_cache_key()

        crumbs = cache.get(cache_key)
        if not crumbs:
            crumbs = self.get_crumbs(context)
            cache.set(cache_key, crumbs, self.cache_timeout)
        return crumbs

    def get_crumbs(self, context):
        raise NotImplementedError

    def render_to_response(self, context, **response_kwargs):
        if hasattr(self.request, 'breadcrumbs'):
            self.request.breadcrumbs(self.get_breadcrumbs(context))
            context['show_crumbs'] = True
        else:
            context['show_crumbs'] = False
        return super(CrumbsMixin, self).render_to_response(
            context, **response_kwargs)

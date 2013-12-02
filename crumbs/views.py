# -*- coding: utf-8 -*-

import hashlib

from django.conf import settings
from django.core.cache import cache
from django.utils.encoding import smart_str
from django.contrib.sites.models import get_current_site


class CrumbsMixin(object):
    cache_prefix = getattr(settings, 'CRUMBS_CACHE_PREFIX', 'CRUMBS')
    cache_timeout = getattr(settings, 'CRUMBS_CACHE_TIMEOUT', 3600)

    def get_cache_key(self):
        current_site = get_current_site(self.request)

        return '%s:%s' % (self.cache_prefix, hashlib.md5(smart_str('%s%s' % (
            current_site.domain, self.request.path_info))).hexdigest())

    def get_crumbs(self, context):
        raise NotImplementedError

    def get_breadcrumbs(self, context):
        cache_key = self.get_cache_key()

        crumbs = cache.get(cache_key)
        if not crumbs:
            crumbs = self.get_crumbs(context)
            cache.set(cache_key, crumbs, self.cache_timeout)
        return crumbs

    def render_to_response(self, context, **response_kwargs):
        if hasattr(self.request, 'breadcrumbs'):
            self.request.breadcrumbs(self.get_breadcrumbs(context))
            context['show_crumbs'] = True
        else:
            context['show_crumbs'] = False
        return super(CrumbsMixin, self).render_to_response(
            context, **response_kwargs)

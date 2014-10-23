# -*- coding: utf-8 -*-

from django.conf import settings

CACHE_PREFIX = getattr(settings, 'CRUMBS_CACHE_PREFIX', 'CRUMBS')
CACHE_TIMEOUT = getattr(settings, 'CRUMBS_CACHE_TIMEOUT', 3600)

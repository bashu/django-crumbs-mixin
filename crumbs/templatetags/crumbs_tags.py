# -*- coding: utf-8 -*-

from django import template

register = template.Library()

def breadcrumbs(context, instance, template_name="breadcrumbs/crumbs.html"):
    return {'object': instance, 'template': template_name, 'crumbs': context['request'].breadcrumbs}

register.inclusion_tag("breadcrumbs/dummy.html", takes_context=True)(breadcrumbs)

# -*- coding: utf-8 -*-


class CrumbsMixin(object):

    def get_crumbs(self, context):
        raise NotImplementedError

    def render_to_response(self, context, **response_kwargs):
        if hasattr(self.request, 'breadcrumbs'):
            self.request.breadcrumbs(self.get_crumbs(context))
            context['show_crumbs'] = True
        else:
            context['show_crumbs'] = False
        return super(CrumbsMixin, self).render_to_response(
            context, **response_kwargs)

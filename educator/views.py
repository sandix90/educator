from django.views.generic import TemplateView
from constance import config


class Main(TemplateView):
    template_name = 'educator/main.html'

    def get_context_data(self, **kwargs):
        kwargs['constance'] = config
        return kwargs

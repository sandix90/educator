from django.urls import reverse
from django.views.generic import TemplateView, FormView, DetailView
from constance import config

from educator.forms import FeedbackForm
from educator.models import Page


class Main(TemplateView):
    template_name = 'educator/main.html'

    def get_context_data(self, **kwargs):
        kwargs['constance'] = config
        return kwargs


class FeedbackView(FormView):
    template_name = 'educator/feedback.html'
    form_class = FeedbackForm
    success_url = '/feedback/success'

    def form_valid(self, form):
        form.instance.save()
        return super(FeedbackView, self).form_valid(form)


class FeedbackSuccessView(TemplateView):
    template_name = 'educator/feedback_success.html'


class PageDetailView(DetailView):
    template_name = 'educator/page.html'
    model = Page


class GalleryView(TemplateView):
    template_name = 'educator/gallery.html'
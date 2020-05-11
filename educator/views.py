from django.urls import reverse
from django.views.generic import TemplateView, FormView, DetailView, ListView
from constance import config

from educator.forms import FeedbackForm
from educator.models import Page, GalleryPhoto, CloudFile


class Main(TemplateView):
    template_name = 'educator/main.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['constance'] = config
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return []


class FeedbackView(FormView):
    template_name = 'educator/feedback.html'
    form_class = FeedbackForm
    success_url = '/feedback/success'

    def form_valid(self, form):
        form.instance.save()
        return super(FeedbackView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(FeedbackView, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [{
            'title': "Обратная связь",
            'url': reverse('feedback')
        }]


class FeedbackSuccessView(TemplateView):
    template_name = 'educator/feedback_success.html'


class PageDetailView(DetailView):
    template_name = 'educator/page.html'
    model = Page

    def get_context_data(self, **kwargs):
        kwargs = super(PageDetailView, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [{
            'title': self.object.title,
            'url': reverse('pages', kwargs={'slug': self.object.slug})
        }]


class GalleryView(ListView):
    template_name = 'educator/gallery.html'
    model = GalleryPhoto

    def get_queryset(self):
        return self.model.objects.filter(enabled=True, page__isnull=True)

    def get_context_data(self, **kwargs):
        kwargs = super(GalleryView, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [{
            'title': 'Галлерея',
            'url': reverse('gallery')
        }]


class CloudFilesDetail(DetailView):
    template_name = 'educator/cloud_file_detail.html'
    model = CloudFile

    def get_context_data(self, **kwargs):
        kwargs = super(CloudFilesDetail, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [{
            'title': self.object.name,
            'url': reverse('cloud_files', kwargs={'slug': self.object.slug})
        }]

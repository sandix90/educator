from django.urls import reverse
from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        kwargs = super(NewsListView, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [{
            'title': 'Новости',
            'url': reverse('news_list')
        }]


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        kwargs = super(NewsDetailView, self).get_context_data(**kwargs)
        kwargs['breadcrumbs'] = self.get_breadcrumbs()
        return kwargs

    def get_breadcrumbs(self):
        return [
            {
                'title': 'Новости',
                'url': reverse('news_list')
            },
            {
                'title': f'{self.object.title[:20]}...',
                'url': reverse('news_detail', kwargs={'pk': self.object.id})
            }
        ]

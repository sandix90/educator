from django.views.generic import ListView, DetailView

from news.models import News


class NewsListView(ListView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'

    def get_queryset(self):
        return self.model.objects.all()


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = News

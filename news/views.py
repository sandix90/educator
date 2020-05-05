from django.views.generic import ListView

from news.models import News


class NewsListView(ListView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'

    def get_queryset(self):
        return self.model.objects.all()


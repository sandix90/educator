from django.urls import path

from news.views import NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list')
]
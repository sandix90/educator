from django import template

from news.models import News

register = template.Library()


@register.inclusion_tag('news_anons.html', name='news_anons')
def get_news_anons():
    news_anons = News.objects.all().order_by('-created_at')[:10]
    return {'news_anons': news_anons}

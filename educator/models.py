from ckeditor.fields import RichTextField
from django.db import models
from autoslug import AutoSlugField


class Feedback(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    sender_name = models.CharField(verbose_name='Отправитель', max_length=255, null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    email = models.CharField(verbose_name='email', max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Отзыв {self.created_at} от {self.sender_name}'

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class Page(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=1000
    )

    content = RichTextField(
        verbose_name='Содержимое',
        blank=True,
    )

    slug = AutoSlugField(
        verbose_name='Короткое имя',
        max_length=1000,
        populate_from='title',
        unique_with='title',
        always_update=False,
        editable=True
    )

    display = models.BooleanField(
        verbose_name='Отображение',
        default=True
    )

    class Meta:
        verbose_name_plural = 'Страницы'
        verbose_name = 'Страница'

    def __str__(self):
        return f'Страница "{self.title[:20]}"'

    def get_absolute_url(self):
        return f'/{self.slug}/'

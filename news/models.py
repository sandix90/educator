from ckeditor.fields import RichTextField
from django.db import models


class News(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text = RichTextField(verbose_name='Текст новости')

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новости'

    def get_anons(self):
        return self.title[:50]

    def __str__(self):
        return self.title[:50]

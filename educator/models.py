from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
        return f'Страница "{self.title[:50]}"'

    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_cloud_files(self):
        return self.cloudfile_set.all()

    def get_page_photos(self):
        return self.galleryphoto_set.filter(enabled=True)


# class Image(models.Model):
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
#     object_id = models.PositiveIntegerField(null=True)
#     content_object = GenericForeignKey("content_type", "object_id")
#
#     # Put it into the e.g. product class
#     def get_images(self) -> List[Image]:
#         content_type = ContentType.objects.get_for_model(self)
#         images = Image.objects.filter(object_id=self.id, content_type=content_type)
#         return images


class GalleryPhoto(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    name = models.CharField(verbose_name='Имя изображения', max_length=255, blank=False, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='gallery')
    enabled = models.BooleanField(verbose_name='Отображать?', default=True)

    page = models.ForeignKey(
        'Page',
        verbose_name='Страница отображения',
        null=True, blank=True,
        on_delete=models.CASCADE,
        help_text='Если страница не указана, картинка будет отображаться в фотогалерее'
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Картинка галлереи'
        verbose_name_plural = 'Картинки галлереи'


class CloudFile(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата создания', auto_now=True)

    name = models.CharField(verbose_name='Имя файла', max_length=255)
    iframe_code = models.TextField(verbose_name='Код html')
    link = models.CharField(verbose_name='Ссылка', max_length=1000)

    page = models.ForeignKey('Page', verbose_name='Страница отображения', null=True, blank=True, on_delete=models.CASCADE)

    slug = AutoSlugField(
        verbose_name='Короткое имя',
        max_length=1000,
        populate_from='name',
        unique_with='name',
        always_update=False,
        editable=True
    )

    class Meta:
        verbose_name = 'Облачный файл'
        verbose_name_plural = 'Облачные файлы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

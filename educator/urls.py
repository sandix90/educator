
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.static import serve

from educator import settings
from educator.views import Main, FeedbackView, FeedbackSuccessView, PageDetailView, GalleryView, CloudFilesDetail

urlpatterns = [
    path('', Main.as_view(), name='main'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback/success', FeedbackSuccessView.as_view(), name='feedback_success'),
    path('files/<slug:slug>/', CloudFilesDetail.as_view(), name='cloud_files'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('<slug:slug>/', PageDetailView.as_view(), name='pages'),
]

admin.site.site_header = 'Мой сайт'

if settings.DEBUG:
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
    urlpatterns += staticfiles_urlpatterns()


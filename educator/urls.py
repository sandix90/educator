
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from educator.views import Main, FeedbackView, FeedbackSuccessView, PageDetailView, GalleryView

urlpatterns = [
    path('', Main.as_view(), name='main'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('feedback/success', FeedbackSuccessView.as_view(), name='feedback_success'),
    path('<slug:slug>', PageDetailView.as_view(), name='pages'),
    path('gallery/', GalleryView.as_view(), name='gallery')
]
urlpatterns += staticfiles_urlpatterns()

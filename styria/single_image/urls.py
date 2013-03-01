from django.conf.urls import patterns, url
from views import AllImagesListView, SingleImageDetailView, UploadImageCreate


urlpatterns = patterns('',
    url(r'^image/(?P<pk>\d+)/$', SingleImageDetailView.as_view(), name='single_image'),
    url(r'^images/(?:(?P<page>\d+)/)?$', AllImagesListView.as_view(), {'sort': 'date'}, name='all_images',),
    url(r'^images/r/(?:(?P<page>\d+)/)?$', AllImagesListView.as_view(), {'sort': 'rating',}, name='all_images_rating',),
    url(r'^$', UploadImageCreate.as_view(), name='upload_image'),
)

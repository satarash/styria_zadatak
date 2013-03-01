from django.conf.urls import patterns, url


urlpatterns = patterns('styria.single_image.views',
    url(r'^image/(?P<pk>\d+)/$', 'single_image', name='single_image'),
    url(r'^images/(?:(?P<page>\d+)/)?$', 'all_images', {'sort': 'date'}, name='all_images',),
    url(r'^images/r/(?:(?P<page>\d+)/)?$', 'all_images_rating', {'sort': 'rating', }, name='all_images_rating', ),
    url(r'^$', 'upload_image', name='upload_image'),
)

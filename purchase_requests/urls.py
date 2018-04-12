from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^purchase_requests/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^purchase_requests$', views.request_new, name='request_new'),
    url(r'^purchase_requests/upload/csv$', views.upload_csv, name='upload_csv'),
    url(r'^delete/(?P<part_id>[0-9]+)/$', views.function, name='delete_view'),
]

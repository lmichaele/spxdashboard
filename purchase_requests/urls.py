from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #sends the purchasing requests page to browser
    #url(r'^purchase_requests/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^purchase_requests/new/$', views.request_new, name='request_new'),
]

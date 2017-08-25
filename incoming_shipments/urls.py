from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^incoming_shipments$', views.incoming_shipments, name='incoming_shipments'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),#sends the purchasing requests page to browser  
]

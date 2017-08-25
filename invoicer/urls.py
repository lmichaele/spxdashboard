from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^invoicer$', views.invoicer, name='invoicer'),
]

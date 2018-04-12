from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^invoicer$', views.invoicer, name='invoicer'),
    url(r'^invoicer/xml_upload$', views.xml_to_csv, name='xml_to_csv'),
    #url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
]

from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^report/new/$', views.new_report, name='new_report'),
	]
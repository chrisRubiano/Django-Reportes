from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^report/new/$', views.new_report, name='new_report'),
        url(r'^calibration/new/$', views.new_calibration, name='new_calibration'),
        url(r'^report_list$', views.report_list, name='report_list'),
	]
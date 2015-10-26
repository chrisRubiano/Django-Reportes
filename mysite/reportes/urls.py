from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.inicio),
        url(r'^report/new/$', views.new_report, name='new_report'),
        url(r'^calibration/new/$', views.new_calibration, name='new_calibration'),
        url(r'^report_list$', views.report_list, name='report_list'),
        url(r'^report/(?P<pk>[0-9]+)/$', views.report_detail, name="report_detail"),
        url(r'^calibration/(?P<pk>[0-9]+)/$', views.calibration_detail, name="calibration_detail"),
        url(r'^calibration_list$', views.calibration_list, name='calibration_list'),
        url(r'^calibration_pending$', views.calibration_pending, name='calibration_pending')
	]
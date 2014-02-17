from django.conf.urls import patterns, url

from healthy_salad_chooser import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
)
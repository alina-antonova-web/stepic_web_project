from django.conf.urls import url, include, patterns

from qa.views import test

urlpatterns = patterns('',
	url(r'^$', test, name='home'),
	url(r'^login/$', test, name='login'),
	url(r'^signup/$', test, name='signup'),
	url(r'^question/(\d+)/$', test, name='question'),
	url(r'^ask/$', test, name='ask'),
	url(r'^popular/$', test, name='popular'),
	url(r'^new/$', test, name='new'),
)

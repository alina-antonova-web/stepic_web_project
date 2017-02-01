from django.conf.urls import url, patterns, include

from qa.views import test

urlpatterns = patterns('qa.views',
	url(r'^$', test, name='home'),
	url(r'^login/$', test, name='login'),
	url(r'^signup/$', test, name='signup'),
	url(r'^question/(\d+)/$', test, name='question'),
	url(r'^ask/$', test, name='ask'),
	url(r'^popular/$', test, name='popular'),
	url(r'^new/$', test, name='new'),
)

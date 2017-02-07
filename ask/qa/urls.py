from django.conf.urls import url, patterns

from qa.views import test

urlpatterns = patterns('qa.views',
	url(r'^$', new_questions_list, name='new_questions_list'),
	url(r'^login/$', test, name='login'),
	url(r'^signup/$', test, name='signup'),
	url(r'^question/(\d+)/$', test, name='question'),
	url(r'^ask/$', test, name='ask'),
	url(r'^popular/$', popular_questions_list, name='popular_questions_list'),
	url(r'^new/$', new_questions_list, name='new_questions_list'),
)

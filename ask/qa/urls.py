from django.conf.urls import url, patterns, include
#from qa.views import test, question_list, question_detail, popular
#from qa.views import question_ask, question_answer
#from qa.views import user_signup, user_login, user_logout

urlpatterns = patterns('qa.views',
    url(r'^$', 'test'),
    url(r'^question/(?P<id>[0-9]+)/$', 'test', name='question_detail'),
    url(r'^popular/.*', 'test', name='popular'),
    url(r'^ask/.*', 'test', name='question_ask'),
    #url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/.*$', 'test', name='signup'),
    url(r'^login/.*$', 'test', name='login'),
    #url(r'^logout/', user_logout, name='logout'),
    url(r'^new/.*', 'test', name='new'),
)
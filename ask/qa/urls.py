from django.conf.urls import url
#from qa.views import test, question_list, question_detail, popular
#from qa.views import question_ask, question_answer
#from qa.views import user_signup, user_login, user_logout

urlpatterns = [
    url(r'^$', 'qa.views', name='question_list'),
    url(r'^question/(?P<pk>\d+)/', 'qa.views', name='question_detail'),
    url(r'^popular/', 'qa.views', name='popular'),
    url(r'^ask/', 'qa.views', name='question_ask'),
    #url(r'^answer/', question_answer, name='question_answer'),
    url(r'^signup/', 'qa.views', name='signup'),
    url(r'^login/', 'qa.views', name='login'),
    #url(r'^logout/', user_logout, name='logout'),
    url(r'^new/', 'qa.views', name='new'),
]
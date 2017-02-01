"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include

from django.contrib import admin
admin.autodiscover()

from qa import views

urlpatterns = [
#    url(r'^', include("qa.urls")),
	url(r'^$', views.test, name='home'),
	url(r'^login', views.test, name='login'),
	url(r'^signup', views.test, name='signup'),
	url(r'^question/(?P<id>\d+)', views.test, name='question'),
	url(r'^ask', views.test, name='ask'),
	url(r'^popular', views.test, name='popular'),
	url(r'^new', views.test, name='new'),
	url(r'^admin/', admin.site.urls),
]

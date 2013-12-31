from django.conf.urls import patterns, url
from jobs import views

urlpatterns = patterns('',
    url(r'^(?P<permalink>.+)/details/$', views.getCompanyInfo, name='getCompanyInfo')
)
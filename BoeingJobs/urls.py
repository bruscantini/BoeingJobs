from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jobs.views.allJobs', name='allJobs'),
    url(r'^deleteAll$', 'jobs.views.deleteAll', name='deleteAll'),
    url(r'^newCompanies$', 'jobs.views.checkForNewCompanies', name='checkForNewCompanies'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^company/', include('jobs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

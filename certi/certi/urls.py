from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'llaves.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'llaves.views.register', name='register'),
    url(r'^validate/$', 'llaves.views.validate', name='validate'),



    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's_shot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home.urls')),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^accounts/', include('registration.urls')),
    #(r'^loginza/', include('loginza.urls')),
)
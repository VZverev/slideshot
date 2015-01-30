# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
from broadcasts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'get_new/$', views.get_new),
    url(r'broadcast(?P<num>\d+)/$', views.slider),
    url(r'$', views.slider),#first public
    
    
)

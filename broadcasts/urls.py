# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
from broadcasts import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'slides', views.SlideViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    # Examples:
    # url(r'^$', 'slide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # примерные адреса:
    #    /channels/
    #    /channel/<id>
    #    /mychannel/
    #    /broadcast/<id>
    
    #примерные адреса api
    #    get_slide/<br>/<pos>
    #    get_slide/<br>
    #    add_slide/
    #    
    url(r'^', include(router.urls)),
    #url(r'^slide_get/(?P<bk>[0-9]+)/(?P<pos>[0-9]+)/$', views.SlideGet.as_view()),
    url(r'^slide_get/$', views.SlideGet.as_view()),
    url(r'^broadcast/(?P<bk>[0-9]+)/$', views.slider),
    url(r'^$', views.slider),#first public
    
    url(r'^channel_list$', views.channel_list),#first public
    url(r'^broadcasting_list$', views.broadcasting_list),#first public
    
    url(r'^broadcasting/(?P<id>[0-9]+)/$', views.broadcasting),
    url(r'^channel/(?P<id>[0-9]+)/$', views.channel),
)

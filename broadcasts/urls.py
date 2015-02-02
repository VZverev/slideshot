# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
from broadcasts import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'slides', views.SlideViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^slide_get/(?P<bk>[0-9]+)/(?P<pos>[0-9]+)/$', views.SlideGet.as_view()),
    url(r'^', include(router.urls)),
    url(r'^get_slide/$', views.get_new),
    url(r'^broadcast(?P<num>\d+)/$', views.slider),
    url(r'^$', views.slider),#first public
)

#! /usr/bin/env python
#coding = utf-8
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^aboutme/$', views.post_simple, name='post_simple'),
    url(r'^xc/$', views.post_xc, name='post_xc'),
    url(r'^shuo/$', views.index_all, name='index_all'),
    ]



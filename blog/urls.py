# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/23.
'''

from django.conf.urls import url
from . import views

# 视图函数命名空间
app_name='blog'
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^search/$',views.search,name='search'),
    url(r'^book/$',views.book,name='book'),
    url(r'^bookmark/$',views.bookmark,name='bookmark'),
    url(r'^about/$',views.about,name='about')
]
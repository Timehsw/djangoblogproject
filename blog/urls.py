# -*- coding: utf-8 -*-
'''
    Created by hushiwei on 2017/9/23.
'''

from django.conf.urls import url
from . import views

# 视图函数命名空间
app_name='blog'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'about$',views.about,name='about')
]
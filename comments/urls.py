# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
'''
    Created by hushiwei on 2017/9/24.
'''

app_name='comments'
urlpatterns=[
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
]